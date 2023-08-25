#Authors: Nana Obeng, Oliver Quaye and Saani Mustapha

from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator =  Nominatim(user_agent="disc")

def calculate(location1, location2):
    location1Lat = (location1.latitude, location1.longitude)
    location2Lat = (location2.latitude, location2.longitude)
    measure = int(geodesic(location1Lat, location2Lat).miles)
    print(f"The distance between the cities is {measure} miles")


while True:
    try:
        x = input("Name of first city: ")
        y = input("Name of second city: ")
        location1 = geolocator.geocode(x)
        location2 = geolocator.geocode(y)

        if location1 is None or location2 is None:
            print("Invalid input. Please provide valid city names.")
        else:
            calculate(location1, location2)
            break
    except Exception as e:
        print("An error occured", e,"\n")
