## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- yo
- Hello
- Hola
- hola

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- see ya
- bye bye

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- cool
- yeah

## intent:restaurant_search
- I'm looking for a place to eat
- Looking for places to eat
- Looking for restaurants
- I'm searching for restaurants
- I'm hungry. Looking out for some good restaurants

## intent:cuisine_check
- [American](cuisine)
- [North Indian](cuisine)


## intent:budget_check
- [low](budget)
- [cheap](budget:low)
- [medium](budget)
- [high](budget)

## intent:send_email
- Yes, send it to my email at [yvss.santosh@gmail.com](email)
- Send to [yvss.santosh@gmail.com](email)
- [abcdefgh@domain.com](email)

## intent:location_search
- [agra](location)
- [bengaluru](location:Bangalore)
- [New Delhi](location:Delhi)
- [Raipur](location)
- [Hubli](location:Hubli-Dharwad)
- [dehradun](location:Dehradun)

## synonym:Bangalore
- bengaluru
- Bengaluru
- bangalore

## synonym:Delhi
- New Delhi
- delhi
- new delhi
- new Delhi
- New delhi
- capital of india
- capital
- dhilli

## synonym:Hubli-Dharwad
- Hubli
- hubli
- Dharwad
- dharwad

## synonym:chinese
- chines
- Chinese
- china

## synonym:low
- cheap
- inexpensive

## synonym:medium
- Medium
- med
- moderate
- mid
- Med
- Moderate
- Mid

## lookup:budget
  data/valid_budget.txt

## lookup:cuisine
  data/valid_cuisines.txt

## lookup:location
  data/valid_cities.txt

## regex:email
- (?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])

## regex:location
- [A-Za-z\s+-]

## regex:cuisine
- [A-Za-z\s]

## regex:budget
- [lowmediumhg]