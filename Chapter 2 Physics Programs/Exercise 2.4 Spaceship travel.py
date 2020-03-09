# Done

#for equation derivation see "Medern Physics For Scientists and Engineers"
#Second Edition, Chapter 1, section 8.
import numpy as np

def how_much_time_does_it_take_to_reach(distance, speed_of_ship_as_fraction_of_light):
    speed_of_light = 299792458.
    distance = float(distance)
    speed_of_ship_as_fraction_of_light = float(speed_of_ship_as_fraction_of_light)

    time_measured_in_the_cockpit = (distance / (speed_of_ship_as_fraction_of_light * speed_of_light))

    time_detected_from_earth = (distance / np.sqrt(speed_of_light**2 - speed_of_ship_as_fraction_of_light** 2))

    return time_measured_in_the_cockpit, time_detected_from_earth

cockpit, earth = how_much_time_does_it_take_to_reach(input("Enter the distance in meters: "), input("Enter the speed of the ship as a fraction of the speed of light: "))

print("This the time measured in the ship: %f s, and this is the time measured on earth: %f s" % (cockpit, earth))



