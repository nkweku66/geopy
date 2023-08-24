#Authors: Nana Obeng, Oliver Quaye and Saani Mustapha

from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator =  Nominatim(user_agent="disc")
x =  input("Name of first city: ")
y = input("Name of second city: ")

location1 = geolocator.geocode(x)
location2 = geolocator.geocode(y)
location1Lat = (location1.latitude, location1.longitude)
location2Lat = (location2.latitude, location2.longitude)
measure = geodesic(location1Lat, location2Lat).miles

print(f"The distance between the cities is {measure} miles")
#print(location2.latitude, location2.longitude)
#def city_name(city1, city2):



#print(geodesic(x,y).miles)
