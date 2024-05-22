cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers # calculates car not driven by taking difference of cars and drivers
cars_driven = drivers # assign drivers value to cars_driven
carpool_capacity = cars_driven + space_in_a_car #calculates the total carpool capacity
average_passengers_per_car = passengers / cars_driven #calculates average passengers per car 

print("There are",cars ,"cars available.")
print("There are only", drivers, "drivers available.")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")