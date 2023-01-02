#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime
import data_manager
import flight_data
import flight_search
import notification_manager
import requests
import json
from dateutil.relativedelta import relativedelta
# from kiwiflightsearch import kiwiparams

#----------------------------  Constants  -------------------------------------------------------------------------------------------------------

# airport3 = input("Enter 3 letter code for where you want to go:")
airport3 = "BCN"

today = datetime.today().strftime('%d/%m/%Y')
six_months = datetime.today() + relativedelta(months=+6)
six_months_later = six_months.strftime('%d/%m/%Y')
flight_from = "LHR"

print(today)
print(six_months_later)

# API Related  Constants
SHEETY_URL = "https://api.sheety.co/7c9e84c70ba179265f92742eed873239/flightDeals/prices"
KIWI_URL = "https://partners.kiwi.com/"
TEQUILA_URL = "https://tequila.kiwi.com/portal/docs/tequila_api"
FLIGHT_SEARCH_URL = "https://api.tequila.kiwi.com/v2/search?"
FLIGHT_PARAMS = "fly_from="+flight_from+"&fly_to="+airport3+"&dateFrom="+today+"&dateTo="+six_months_later
# LONG_FLIGHT_PARAMS = kiwiparams

headers = {
    "apikey" : "sxKBxvRUFqfKRBr0T0NfnwBs2WcVeNYB"
}

SMS_URL = "https://www.twilio.com/docs/sms"

sheet_data = requests.get(SHEETY_URL)
sheet_data.raise_for_status()

flights = requests.get(FLIGHT_SEARCH_URL, params=FLIGHT_PARAMS, headers=headers)
flights.raise_for_status()

# print(f"This is the JSON Parsed data: \n {r.json()}")
# print(f"This is the flights data: \n {flights.json()}\n")


# The return JSON has got a search id, with a list of data items per flight.  So...
flights_json = json.loads(flights.text)
# This makes a list of the flight data items only
flight_data = flights_json['data']
# print(type(flight_data))

flight_details = {}
lowest_price = 99999999
# Then for each flight, we want to just grab some key bits of information.
for flight in flight_data:
    # print(flight_data['id'])
    # print(type(flight))
    # print(flight['id'])
    # print(flight['cityTo'])
    # print(flight['price'])

    if flight['price'] < lowest_price:
        lowest_price = flight['price']

        flight_details['id'] = flight['id']
        flight_details['flyTo'] = flight['flyTo']
        flight_details['price'] = flight['price']
        flight_details['flyfrom'] = flight['flyFrom']
        flight_details['countryFrom'] = flight['countryFrom']
        flight_details['airlines'] = flight['airlines']
        flight_details['cityTo'] = flight['cityTo']
        flight_details['countryTo'] = flight['countryTo']
        flight_details['route'] = flight['route']
        flight_details['routeline'] = flight['route'][0]['airline']
    # print("")

print(json.dumps(flight_details, indent=4))
print(flight_details.keys)