#Prime Number Program by Naomi Keller. Version 1.2, last updated 3/22/2019
#Program determines if a number is prime.
#VARIABLES:
#num: variable in functions used to compare
#numb: input from user to be used in functions and output

from math import sqrt

# Making sure number is integer, not decimal etc.
def isInt(num):
    return num // 1 == num

def isPrime(num):
    # 2 is the lowest prime number, if it below it isn't prime.
    if num < 2:
        return False
    # Since 2 is lowest, starting from 2 it checks if the number can be divided by
    # anything other than itself by stopping at the square root of the number.
    i = 2
    while i <= sqrt(num):
        if isInt(num / i):
            return False
        i += 1
    return True

print(2, end='')
for i in range(3, 100):
    if isPrime(i):
        print(', ' + str(i), end='')
print()


### this was I/O code for 17 ###
# numb = int(input('Enter a positive integer: '))
# if isPrime(numb):
   # print(str(numb) + ' is a prime number.')
# else:
   # print(str(numb) + ' is not a prime number.')
