import os
import json
from datetime import datetime
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from typing import Dict, Text, Any, List, Union, Optional

# Custom imports
from utils.formatter import restaurant_formatter_sorter
from utils.send_email import send_email
from utils import zomato_api as zomatopy


class RestaurantForm(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "restaurant_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return [
            "location",
            "cuisine",
            "budget",
        ]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "location": [self.from_entity(entity="location"), self.from_text()],
            "cuisine": [self.from_entity(entity="cuisine"), self.from_text()],
            "budget": [self.from_entity(entity="budget"), self.from_text()],
        }

    def validate_cuisine(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """
        Checks if the cuisines are a part of:
        1. American         4. Mexican
        2. Chinese          5. North Indian
        3. Italian          6. South Indian
        """
        cuisine_list = [
            "american",
            "chinese",
            "italian",
            "mexican",
            "north indian",
            "south indian",
        ]
        print("########## cuisine value is : ", value)
        if value.lower() not in cuisine_list:
            dispatcher.utter_message(template="utter_wrong_cuisine")
            return {"cuisine": None}
        return {"cuisine": value}

    def validate_location(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """
        Checks if the given locations are part of TIER-I & TIER-II cities
        """
        location_list = open("./data/valid_cities.txt").read().split("\n")
        print("########## Location value is : ", value)
        if value.lower() not in location_list:
            dispatcher.utter_message(template="utter_locationNotServiced")
            return {"location": None}
        return {"location": value}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """
        Queries Zomato API based on parameters cuisine, location.
        
        Saves the result data to a file based on timestamp which will
        be used later to send email listing top 10 restaurants to the customer
        """

        # Zomato API Config
        config = {"user_key": os.getenv("ZOMATO_API_KEY")}
        zomato = zomatopy.initialize_app(config)

        # Loading data from slots
        loc = tracker.get_slot("location")
        cuisine = tracker.get_slot("cuisine")
        budget = tracker.get_slot("budget")

        # Processing the data obtained
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {
            "american": 1,
            "chinese": 25,
            "north indian": 50,
            "italian": 55,
            "mexican": 73,
            "south indian": 85,
        }

        # Querying Restaurants using Zomato API
        results = zomato.restaurant_search(
            "", lat, lon, str(cuisines_dict.get(cuisine)), limit=30
        )

        d = json.loads(results)
        if d["results_found"] == 0:
            response = "No Results"
            dispatcher.utter_message("-----" + response)
            return []

        # Formatting, Sorting (by rating) and Saving the Restaurant
        # data obtained to a file for data propogation to different intent
        restaurants = restaurant_formatter_sorter(
            zomato.filter_restaurants_by_budget(budget, d["restaurants"])
        )

        # Save only top 10 restaurants to the file because current requirement states
        # to send top 10 restaurants to customer via email, thus improving efficiency
        file_path = "data/restaurants/restaurants-{}.json".format(
            datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        )
        open(file_path, "w").write(json.dumps(restaurants[:10]))

        # Printing top 5 restaurants
        response = "\nRestaurant List\n\n"
        for restaurant in restaurants[:5]:
            response += "{} in {} has been rated {} with an average cost for two being {}\n\n".format(
                restaurant["name"],
                restaurant["address"],
                restaurant["rating"],
                restaurant["cost_for_two"],
            )

        dispatcher.utter_message(response)

        # Returning back the newly added data `restaurants_file`
        return [SlotSet("restaurants_file", file_path.split("/")[2])]


class ActionSendEmail(Action):
    """
    Sends top 10 restaurants as an email to the user and once
    the email has been sent, delete the file which was created
    to store the restaurant data
    """

    def name(self):
        return "action_send_email"

    def run(self, dispatcher, tracker, domain):
        email = tracker.get_slot("email")

        # Load data from file
        restaurants_file_path = "data/restaurants/{}".format(
            tracker.get_slot("restaurants_file")
        )
        restaurant_data = json.loads(open(restaurants_file_path).read())

        # Call send email method
        response = send_email(email, restaurant_data)

        # Sending sucess response and deleting the file
        # for a success response
        response = (
            "Sucessfully sent email!" and os.remove(restaurants_file_path)
            if response == 202
            else "Sorry!! Unable to send email right now! Will be processed soon!"
        )

        dispatcher.utter_message(response)
