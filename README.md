# Foodie Bot

This is a chat bot built using RASA framework

### Environment Variables to Load

```sh
export ZOMATO_API_KEY=VALUE
export SENDGRID_API_KEY=VALUE

```

### Project Setup

```sh
# Setup a virtual environment.
# This project has been run and tested on python3.7.5
# so make sure python3 --> python3.7.5
mkvirtualenv foodie_bot -p python3

# For existing virtual environments
workon foodie_bot

# First, install the requirements as we're using sendgrid 
# to send email and tensorflow-text library as well
(foodie_bot) pip install -r requirements.txt

# Train the core model
(foodie_bot) rasa train core

# Run rasa shell
(foodie_bot) rasa shell

# Run interactive shell to test the model flow and perform
# live edits on the model. The files stories.md, nlu.md and domain.yml
# are automatically updated based on the newly tested flows (if any)
(foodie_bot) rasa interactive
```