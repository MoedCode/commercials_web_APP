#!/usr/bin/env python3
import sys
import os

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to the system path
parent_directory = os.path.join(script_directory, '..')
sys.path.append(parent_directory)
from modules.base import Base
import phonenumbers
from geopy.geocoders import Nominatim

def _validate_phone_number( value, country):
    if value is None:
        raise ValueError("Phone number is required ")


    if not isinstance(value, str):
        value = str(value)
            # Parse the phone number
    try:
        parsed_number = phonenumbers.parse(value, country)
    except phonenumbers.phonenumberutil.NumberParseException as e:
        raise ValueError(f"Invalid phone number: {str(e)}")

            # Validate the phone number
    if not phonenumbers.is_valid_number(parsed_number):
        raise ValueError("Invalid phone number")
    return value

# x = _validate_phone_number("+211100783735", "Egypt")
# print(f"phone {x}")
x = Base()
print(f"::------->> {x}")
def _validate_city_country(city, country):
    if city is None or country is None:
        raise ValueError("City and country are required")

    geolocator = Nominatim(user_agent="my_app")

    # Construct the address string
    address = f"{city}, {country}"

    # Geocode the address with language parameter set to English
    location = geolocator.geocode(address, language="en")
    print(f" :: location >> {location}")
    print(f" :: location.row >> {location.raw}")
    print(f" :: location.row >> {location.raw['display_name']}")

    # Check if the location was found
    if location is None:
        raise ValueError("Location not found for the provided city and country")

    # Check if the city exists in the response
    if city.lower() not in location.raw['display_name'].lower() and country.lower() not in location.raw['display_name'].lower():
        raise ValueError("City not found in the response")

    # Normalize the city names for comparison
    # response_city = location.raw["address"]["city"].lower()
    # input_city = city.lower()

    # if response_city != input_city:
    #     raise ValueError("City not found in the response")

    return city.lower().capitalize(), country.lower().capitalize()

print("\n\n RESULT \n\n",_validate_city_country("osaka", "japan")[0])


