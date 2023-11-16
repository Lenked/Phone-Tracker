# track location and time zone using the phone number
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

number = input("Entrer le numero de telephone avec le code du pays : ")

# Parsing String to the Phone number
phoneNumber = phonenumbers.parse(number)

# printing the timezone using the timezone module
timeZone = timezone.time_zones_for_number(phoneNumber)
print("Emplacement : " + str(timeZone))

# printing the geolocation of the given number using the geocoder module
geolocation = geocoder.description_for_number(phoneNumber, "en")
print("Localisation : " + geolocation)

# printing the service provider name using the carrier module
service = carrier.name_for_number(phoneNumber, "en")
print("Nom du fournisseur : " + service)
