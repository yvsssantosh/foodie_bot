# Foodie Bot

This is a chat bot built using RASA framework

### Aim
The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience

The bot takes the following inputs from the user:
1. **City:** Take the input from the customer as a text field

    Example:

        Bot: In which city are you looking for restaurants?
        User: anywhere in Delhi
    The chatbot provides results for tier-1 and tier-2 cities only, while for tier-3 cities, it replies back with something like "We do not operate in that area yet".

2. **Cuisine Preference:** This is an input taken from the customer. The bot will list out the following six cuisine categories (Chinese, Mexican, Italian, American, South Indian & North Indian) and the customer can select any one out of that. For this I've used Buttons. More on this can be found [here](https://rasa.com/docs/rasa/core/slots/#slots-set-by-clicking-buttons).

    Example:
    
    ```
    Bot: What kind of cuisine would you prefer?
    * Chinese
    * Mexican
    * Italian
    * American
    * South Indian
    * North Indian

    User: I’ll prefer Italian!
    ```

    ### Important Notes: 

    1. We have assumed that Foodie works only in Tier-1 and Tier-2 cities. You can use the current HRA classification of the cities from [here](https://en.wikipedia.org/wiki/Classification_of_Indian_cities). Under the section 'current classification' on this page, the table categorizes cities as X, Y and Z. Consider 'X ' cities as tier-1 and 'Y' as tier-2. 
    2. The bot can identify common synonyms of city names, such as Bangalore/Bengaluru, Mumbai/Bombay etc.

3. **Average budget for two people:** The price range (average budget for two people) is segmented into three categories: lesser than 300, 300 to 700 and more than 700. The bot asks the user to select one of the three price categories. Even for this we've used [Rasa Buttons](https://en.wikipedia.org/wiki/Classification_of_Indian_cities)

While showing the results to the user, the bot displays the top 5 restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 5 being the highest). The format used for that is: 

`{restaurant_name} in {restaurant_address} has been rated {rating}.`

Finally, the bot will ask the user whether he/she wants the details of the top 10 restaurants on email. If the user replies 'yes', the bot takes user’s email as input and mails via the Sendgrid API using the template `utils/email_template.html`(Note that this part is configured directly in sendgrid). If the user says no, then the bot replies with a goodbye message. The mail has the following details for each restaurant:

* Restaurant Name
* Restaurant locality address
* Average budget for two people
* Zomato user rating

### Environment Variables to Load
Note that before running the project you need to make sure to set these environment variables, else you won't be able to send email or search for restaurants

```sh
# Zomato API Key
export ZOMATO_API_KEY=VALUE

# Sendgrid API key to be able to send emails
export SENDGRID_API_KEY=VALUE

# Since the data obtained from restaurants is a filtered json
# we'll be using email templates to send email

# An example is included in utils/email_template.html
export SENDGRID_TEMPLATE_ID=VALUE

# From email to be shown in the email sent
export FROM_EMAIL=VALUE
```

### Installation

```sh
# Setup a virtual environment.
# This project has been run and tested on python3.7.5
# so make sure python3 --> python3.7.5
mkvirtualenv foodie_bot -p python3

# For existing virtual environments
workon foodie_bot

# Installing spacy
(foodie_bot) pip install spacy

# Downloading and linking en_core_md model
(foodie_bot) spacy download en_core_web_md
(foodie_bot) spacy link en_core_web_md en

# Installing rasa x
(foodie_bot) pip install rasa-x --extra-index-url https://pypi.rasa.com/simple

# Installing sendgrid (for emails)
(foodie_bot) pip install sendgrid

```

`Note: ` Running `pip freeze > requirements.txt` and doing a `pip install -r requirements.txt` won't work for this project because rasa can be installed only using the command mentioned above and spacy library has to be linked properly

### Project Setup

Once we have installed all the libraries, train your model using the command
```sh
# Train nlu model
(foodie_bot) rasa train nlu

# Test the nlu model
# Note: Since the latest model built is an `nlu` model, rasa
# shell will load the nlu model instead of the `core` model
(foodie_bot) rasa shell

# To test the nlu model, type a sample line
# and the model should be able to detect intents, entities, etc
# Ex: I'm looking for restaurants in bombay

# Response

# {
#   "intent": {
#     "name": "restaurant_search",
#     "confidence": 0.8652969609579971
#   },
#   "entities": [
#     {
#       "start": 31,
#       "end": 37,
#       "value": "mumbai",
#       "entity": "location",
#       "confidence": 0.9193029118424353,
#       "extractor": "CRFEntityExtractor",
#       "processors": [
#         "EntitySynonymMapper"
#       ]
#     }
#   ],
#   "intent_ranking": [
#     {
#       "name": "restaurant_search",
#       "confidence": 0.8652969609579971
#     },
#     {
#       "name": "cuisine_check",
#       "confidence": 0.048214756086534
#     },
#     {
#       "name": "location_search",
#       "confidence": 0.040591772082937266
#     },
#     ...
#     ...
#     ...
#   ],
#   "text": "I'm looking for restaurants in bombay"
# }

# Train core model
(foodie_bot) rasa train core

# Run rasa shell to test the model built
# Note: This will the bot, as the latest training was done 
# on the `core` model.
(foodie_bot) rasa shell


# Alternatively, we can run interactive shell to test the model flow and perform
# live edits on the model. The files stories.md, nlu.md and domain.yml will
# be automatically updated based on the newly tested flows (if any)
(foodie_bot) rasa interactive
```

Feel free to create issues [here](https://github.com/yvsssantosh/foodie_bot/issues)