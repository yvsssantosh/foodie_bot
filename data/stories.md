## Complete Story Working #latest
* greet
    - utter_greet
* restaurant_search
    - utter_askLocation
* location_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - utter_askCuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - utter_askBudget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-25-21-15-43.json"}
    - utter_askSendEmail
* affirm
    - utter_enterEmail
* send_email{"email": "abcdefgh@domain.com"}
    - slot{"email": "abcdefgh@domain.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## Story without email
* greet
    - utter_greet
* restaurant_search
    - utter_askLocation
* location_search{"location": "Dehradun"}
    - slot{"location": "Dehradun"}
    - action_check_location
    - utter_askCuisine
* cuisine_check{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_check_cuisine
    - utter_askBudget
* budget_check{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-26-03-42-47.json"}
    - utter_askSendEmail
* send_email
    - utter_enterEmail
* send_email{"email": "yvss.santosh@gmail.com"}
    - slot{"email": "yvss.santosh@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart
