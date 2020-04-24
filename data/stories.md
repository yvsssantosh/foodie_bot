## Complete path
* greet
    - utter_greet
* restaurant_search
    - utter_askLocation
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_check_location
    - utter_askCuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - utter_askBudget
* restaurant_search{"budget": "med"}
    - slot{"budget": "med"}
    - action_search_restaurants
    - utter_askSendEmail
* restaurant_search{"email": "abcde@gmail.com"}
    - slot{"email": "abcde@gmail.com"}
    - action_send_email
    - utter_goodbye
    - export

## bot challenge
* bot_challenge
  - utter_iamabot

## Complete Path #2
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi"}
    - utter_askCuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine": "American"}
    - utter_askBudget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_askSendEmail
* restaurant_search{"email": "abcdef@gmail.com"}
    - slot{"email": "abcdef@gmail.com"}
    - action_send_email
    - utter_goodbye

## Complete Path #3
* greet
    - utter_greet
* restaurant_search
    - utter_askLocation
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_check_location
    - slot{"location": "Hyderabad"}
    - utter_askCuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_check_cuisine
    - slot{"cuisine": "South Indian"}
    - utter_askBudget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - utter_askSendEmail
* restaurant_search{"email": "qwerty@gmail.com"}
    - slot{"email": "qwerty@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kondapur"}
    - slot{"location": "kondapur"}
    - action_check_location
    - slot{"location": ""}
    - utter_locationNotServiced
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - utter_askCuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - slot{"cuisine": "Mexican"}
    - utter_askBudget
* restaurant_search
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - utter_askSendEmail
* restaurant_search{"email": "something@gmail.com"}
    - slot{"email": "something@gmail.com"}
    - action_send_email
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_askLocation
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location": "Bangalore"}
    - utter_askCuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"cuisine": "Italian"}
    - utter_askBudget
* restaurant_search
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_askSendEmail
* restaurant_search{"email": "sample_email@somedomain.com"}
    - slot{"email": "sample_email@somedomain.com"}
    - action_send_email
    - utter_goodbye
    - action_restart
