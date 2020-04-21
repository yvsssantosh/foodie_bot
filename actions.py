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


from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from utils import zomato_api as zomatopy
import json


class ActionSearchRestaurants(Action):
    def name(self):
        return "action_search_restaurants"

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "f4924dc9ad672ee8c4f8c84743301af5"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot("location")
        cuisine = tracker.get_slot("cuisine")
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
