import requests
import ast

base_url = "https://developers.zomato.com/api/v2.1/"


def initialize_app(config):
    return Zomato(config)


class Zomato:
    def __init__(self, config):
        self.user_key = config["user_key"]

    def restaurant_search(
        self, query="", latitude="", longitude="", cuisines="", limit=30
    ):
        """
        Takes either query, latitude and longitude or cuisine as input.
        Returns a list of Restaurant IDs.
        """
        cuisines = "%2C".join(cuisines.split(","))
        if str(limit).isalpha() == True:
            raise ValueError("LimitNotInteger")
        headers = {"Accept": "application/json", "user-key": self.user_key}
        r = (
            requests.get(
                base_url
                + "search?q="
                + str(query)
                + "&count="
                + str(limit)
                + "&lat="
                + str(latitude)
                + "&lon="
                + str(longitude)
                + "&cuisines="
                + str(cuisines),
                headers=headers,
            ).content
        ).decode("utf-8")
        return r  # a = ast.literal_eval(r)

    def get_location(self, query="", limit=5):
        """
        Takes either query, latitude and longitude or cuisine as input.
        Returns a list of Restaurant IDs.
        """
        if str(limit).isalpha() == True:
            raise ValueError("LimitNotInteger")
        headers = {"Accept": "application/json", "user-key": self.user_key}
        r = (
            requests.get(
                base_url + "locations?query=" + str(query) + "&count=" + str(limit),
                headers=headers,
            ).content
        ).decode("utf-8")
        return r

    def filter_restaurants_by_budget(self, budget, restaurants):
        """
        Takes budget, restaurants list and filters the list of restaurants
        based on the budget of user.
        """
        budget_filter = {
            "low": list(
                filter(
                    lambda restaurant: restaurant["restaurant"]["average_cost_for_two"]
                    < 300,
                    restaurants,
                )
            ),
            "medium": list(
                filter(
                    lambda restaurant: 300
                    < restaurant["restaurant"]["average_cost_for_two"]
                    < 700,
                    restaurants,
                )
            ),
            "high": list(
                filter(
                    lambda restaurant: restaurant["restaurant"]["average_cost_for_two"]
                    > 700,
                    restaurants,
                )
            ),
        }
        return budget_filter.get(budget)


class DotDict(dict):
    """
    Dot notation access to dictionary attributes
    """

    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
