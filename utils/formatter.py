new_data = []


def restaurant_formatter_sorter(restaurants):
    """
    # Method to format and sort the restaurant details,
    # where sorting is done based on rating. During formatting the
    # data, only name, address, cost_for_two and rating are saved
    # and rest are discarded as they are not used anywhere else

    # Can be customized based on the requirement which also helps to
    # limit the data being shared with the user
    """
    for restaurant in restaurants:
        new_restaurant = {}

        new_restaurant.update({"name": restaurant["restaurant"]["name"]})
        new_restaurant.update(
            {"address": restaurant["restaurant"]["location"]["address"]}
        )
        new_restaurant.update(
            {"cost_for_two": restaurant["restaurant"]["average_cost_for_two"]}
        )
        new_restaurant.update(
            {"rating": restaurant["restaurant"]["user_rating"]["aggregate_rating"]}
        )

        new_data.append(new_restaurant)

    return sorted(new_data, key=lambda x: x["rating"], reverse=True)
