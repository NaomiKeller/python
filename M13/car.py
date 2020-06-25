'''
Car Speed Class by Naomi Keller. Version 0.5,
last updated 4/19/2019.
This is the class used by test_car.py to calculate the speed of the car.
'''
class Car:
    def __init__(self, make, year_model):
        self.__make = make
        self.__year_model = year_model #aren't these seperate things?
        self.__speed = 0
        
    def accel(self):
        self.__speed += 5
    
    def brake(self):
        self.__speed -= 5
        
    def get_speed(self):
        return self.__speed
