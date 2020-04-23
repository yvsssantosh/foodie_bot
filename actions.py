# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# Default imports
import os
import json
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

# Custom imports
from utils import zomato_api as zomatopy


class ActionSearchRestaurants(Action):
    def name(self):
        return "action_search_restaurants"

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": os.getenv("ZOMATO_API_KEY")}
        zomato = zomatopy.initialize_app(config)

        # Loading data from slots
        loc = tracker.get_slot("location")
        cuisine = tracker.get_slot("cuisine")
        budget = tracker.get_slot("budget")

        budget_dict = {
            "low": budget < 300,
            "medium": 300 < budget < 700,
            "high": budget > 700,
        }

        # Processing the data obtained
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {
            "bakery": 5,
            "chinese": 25,
            "cafe": 30,
            "italian": 55,
            "biryani": 7,
            "north indian": 50,
            "south indian": 85,
        }
        results = zomato.restaurant_search(
            "", lat, lon, str(cuisines_dict.get(cuisine)), 5
        )
        d = json.loads(results)
        response = ""
        if d["results_found"] == 0:
            response = "no results"
        else:
            for restaurant in d["restaurants"]:
                response = (
                    response
                    + "Found "
                    + restaurant["restaurant"]["name"]
                    + " in "
                    + restaurant["restaurant"]["location"]["address"]
                    + "\n"
                )
        dispatcher.utter_message("-----" + response)
        return [SlotSet("location", loc)]


class ActionCheckLocation(Action):
    def name(self):
        return "action_check_location"

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot("location")
        location_list = json.loads(open("valid_cities.json").read())
        if location not in location_list:
            dispatcher.utter_message("Sorry location not found")
            return [SlotSet("location", "")]
        return [SlotSet("location", location)]


class ActionCheckCuisine(Action):
    def name(self):
        return "action_check_cuisine"

    def run(self, dispatcher, tracker, domain):
        cuisine = tracker.get_slot("cuisine")
        cuisine_list = [
            "chinese",
            "mexican",
            "italian",
            "american",
            "south indian",
            "north indian",
        ]
        if cuisine.lower() not in cuisine_list:
            dispatcher.utter_message("Sorry cuisine not found")
            return [SlotSet("cuisine", "")]
        return [SlotSet("cuisine", cuisine)]


class ActionSendEmail(Action):
    def name(self):
        return "action_send_email"

    def run(self, dispatcher, tracker, domain):
        email = tracker.get_slot("email")
        print(f"Sending email to : {email}")
        # TODO: Call send email method
        response = "Sucessfully sent email!"
        dispatcher.utter_message(response)
