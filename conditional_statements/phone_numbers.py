import phonenumbers
import python_basics.location

from phonenumbers import geocoder, timezone, carrier
from python_basics.location import geolocation

def get_phone(phone_number):
    parsed_number = phonenumbers.parse(phone_number, region=None)
    print(geolocation())


phone_number = '+359882931500'


