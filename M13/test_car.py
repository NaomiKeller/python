'''
Car Speed Test Program by Naomi Keller. Version 0.9,
Last updated 4/19/2019.
This program uses the car.py file to track the speed of a car.
'''
#Importing car class from car.py
from car import Car
#Assigning car variable to car class with arguments
car = Car('Acura', '2002 NSX-R')

#print for format purposes
print('Time:        Speed:')
#acceleration loop, lasts 5 iterations
#uses accel and get_speed from class
for i in range(5):
    car.accel()
    speed = car.get_speed()
    print(format(i+1, '4d'), format(speed, '13d'))
#decelleration loop, 5 more iterations
#uses brake and get_speed from class
for i in range(5):
    car.brake()
    speed = car.get_speed()
    print(format(i+6, '4d'), format(speed, '13d'))
