#Authors: Nana Obeng, Oliver Quaye and Saani Mustapha
from gpiozero import Button, LED
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import math

led = LED(21)
led1 = LED(20)
button = Button(2)

geolocator =  Nominatim(user_agent="disc")

def calculate(location1, location2):
    print("Please press the button to calculate")
    button.wait_for_press()
    location1Lat = (location1.latitude, location1.longitude)
    location2Lat = (location2.latitude, location2.longitude)
    measure = math.ceil(geodesic(location1Lat, location2Lat).miles)
    print(f"The distance between the cities is {measure} miles")


while True:
    try:
        x = input("Name of first city: ")
        y = input("Name of second city: ")
        location1 = geolocator.geocode(x)
        location2 = geolocator.geocode(y)

        if location1 is None or location2 is None:
            led.blink(0.5, 0.5)
            print("Invalid input. Please provide valid city names.")
        else:
            led.off()
            led1.on()
            calculate(location1, location2)
            break
    except Exception as e:
        print("An error occured", e,"\n")
