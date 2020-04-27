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

## Story: With yes, then entering email
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

## Story: Without email address
* greet
    - utter_greet
* restaurant_search
    - utter_askLocation
* location_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - utter_askCuisine
* cuisine_check{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_check_cuisine
    - utter_askBudget
* budget_check{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-27-01-47-56.json"}
    - utter_askSendEmail
* deny
    - utter_goodbye
    - action_restart

## Story: With location denial once and remaining entered properly
<!-- In which location? -> Kondapur -->
* greet
    - utter_greet
* restaurant_search
    - utter_askLocation
* location_search{"location": "Kondapur"}
    - slot{"location": "Kondapur"}
    - action_check_location
    - slot{"location": null}
* location_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_check_location
    - utter_askCuisine
* cuisine_check{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_check_cuisine
    - slot{"cuisine": "Chinese"}
    - utter_askBudget
* budget_check{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-27-02-53-50.json"}
    - utter_askSendEmail
* send_email{"email": "beneyaz.cet@gmail.com"}
    - slot{"email": "beneyaz.cet@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## Story: With invalid location, corrected to new location
<!-- Looking for restaurants in Rishikesh -->
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"location": null}
* location_search{"location": "Ahmedabad"}
    - slot{"location": "Ahmedabad"}
    - action_check_location
    - utter_askCuisine
* cuisine_check{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"cuisine": "Italian"}
    - utter_askBudget
* budget_check{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-27-03-11-16.json"}
    - utter_askSendEmail
* affirm
    - utter_enterEmail
* send_email{"email": "yvss.santosh@gmail.com"}
    - slot{"email": "yvss.santosh@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## Story: Cuisine -> chines
* greet
    - utter_greet
* restaurant_search
    - utter_askLocation
* location_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - action_check_location
    - utter_askCuisine
* cuisine_check{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_check_cuisine
    - slot{"cuisine": "Chinese"}
    - utter_askBudget
* budget_check{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-27-17-48-23.json"}
    - utter_askSendEmail
* deny
    - utter_goodbye
    - action_restart

## Story: Restaurant with valid name in first case
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - utter_askCuisine
* cuisine_check{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine": "American"}
    - utter_askBudget
* budget_check{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-27-17-53-35.json"}
    - utter_askSendEmail
* affirm
    - utter_enterEmail
* send_email{"email": "qwerty_name04@gmail.com"}
    - slot{"email": "qwerty_name04@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## Story: Cuisine and Location together
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese", "location": "Chandigarh"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Chandigarh"}
    - action_check_location
    - action_check_cuisine
    - slot{"cuisine": "Chinese"}
    - utter_askBudget
* budget_check{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-27-18-16-38.json"}
    - utter_askSendEmail
* deny
    - utter_goodbye
    - action_restart

## Story: All in one story
* greet
    - utter_greet
* restaurant_search{"budget": "low", "cuisine": "Mexican", "location": "Shimla"}
    - slot{"budget": "low"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Shimla"}
    - action_check_location
    - action_check_cuisine
    - slot{"cuisine": "Mexican"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-27-18-34-44.json"}
    - utter_askSendEmail
* deny
    - utter_goodbye
    - action_restart

## Story: Buget location together
* greet
    - utter_greet
* restaurant_search{"budget": "high", "location": "rajkot"}
    - slot{"budget": "high"}
    - slot{"location": "rajkot"}
    - action_check_location
    - utter_askCuisine
* cuisine_check{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_check_cuisine
    - slot{"cuisine": "italian"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-27-18-46-58.json"}
    - utter_askSendEmail
* affirm
    - utter_enterEmail
* send_email{"email": "my_head_bigger@facebook.com"}
    - slot{"email": "my_head_bigger@facebook.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## Story: cuisine location together
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "salem"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "salem"}
    - action_check_location
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_askBudget
* budget_check{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-27-18-55-26.json"}
    - utter_askSendEmail
* deny
    - utter_goodbye
    - action_restart

## Story : Budget location together
    - utter_greet
* restaurant_search{"budget": "high", "location": "goa"}
    - slot{"budget": "high"}
    - slot{"location": "goa"}
    - action_check_location
    - utter_askCuisine
* cuisine_check{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"cuisine": "south indian"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-27-18-57-32.json"}
    - utter_askSendEmail
* affirm
    - utter_enterEmail
* send_email{"email": "yadavalli.ext@grofers.com"}
    - slot{"email": "yadavalli.ext@grofers.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kurnool"}
    - slot{"location": "kurnool"}
    - action_check_location
    - utter_askCuisine
* cuisine_check{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_askBudget
* budget_check{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - utter_sorry_norestaurants
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"budget": "high", "cuisine": "american", "location": "nanded"}
    - slot{"budget": "high"}
    - slot{"cuisine": "american"}
    - slot{"location": "nanded"}
    - action_check_location
    - action_check_cuisine
    - slot{"cuisine": "american"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-27-20-21-55.json"}
    - utter_askSendEmail
* send_email{"email": "yadav.mnopq@google.com"}
    - slot{"email": "yadav.mnopq@google.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "jalandhar"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "jalandhar"}
    - action_check_location
    - action_check_cuisine
    - slot{"cuisine": "north indian"}
    - utter_askBudget
* budget_check{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-27-20-56-59.json"}
    - utter_askSendEmail
* send_email{"email": "wolfram123alpha@gmail.com"}
    - slot{"email": "wolfram123alpha@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "shimla"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "shimla"}
    - action_check_location
    - action_check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_askBudget
* budget_check{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-27-21-00-25.json"}
    - utter_askSendEmail
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* chitchat
    - utter_cantUnderstand
* restaurant_search
    - utter_askLocation
* send_email{"location": "rajahmundry"}
    - slot{"location": "rajahmundry"}
    - action_check_location
    - utter_askCuisine
* cuisine_check{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_check_cuisine
    - slot{"cuisine": "north indian"}
    - utter_askBudget
* budget_check{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-27-21-10-10.json"}
    - utter_askSendEmail
* deny
    - utter_goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "relangi"}
    - slot{"location": "relangi"}
    - action_check_location
    - slot{"location": null}
* location_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - utter_askCuisine
* cuisine_check{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_check_cuisine
    - slot{"cuisine": "south indian"}
    - utter_askBudget
* budget_check{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-27-21-12-17.json"}
    - utter_askSendEmail
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "bokaro steel city"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bokaro steel city"}
    - action_check_location
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_askBudget
* budget_check{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-27-21-47-21.json"}
    - utter_askSendEmail
* chitchat
    - utter_cantUnderstand
* send_email
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "kollam"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "kollam"}
    - action_check_location
    - action_check_cuisine
    - slot{"cuisine": "north indian"}
    - utter_askBudget
* budget_check{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-27-21-51-12.json"}
    - utter_askSendEmail
* deny
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_askLocation
* send_email{"location": "kondapur"}
    - slot{"location": "kondapur"}
    - action_check_location
    - slot{"location": null}
* stop
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"budget": "medium", "cuisine": "chinese"}
    - slot{"budget": "medium"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_askLocation
* location_search{"location": "gulbarga"}
    - slot{"location": "gulbarga"}
    - action_check_location
    - action_search_restaurants
    - slot{"restaurants_file": "restaurants-2020-04-27-21-59-54.json"}
    - utter_askSendEmail
* deny
    - utter_goodbye
    - action_restart
