#Greater Of Two program by Naomi Keller. Version 2.1, last updated 3/22/2019
#This program finds which of two integers are of the highest value
#VARIABLES:
#num1, num2 = two numbers input by user
#int1, int2 = becomes the num variables inside the max function to be compared.
print('We will determine which of two integers is greater.')
num1 = int(input('Enter the first integer: '))
num2 = int(input('Enter the second integer: '))

def max(int1, int2):
    if int1 > int2:
        return int1
    else:
        return int2

print('\nThe greater integer is', str(max(num1, num2)) + '.')
