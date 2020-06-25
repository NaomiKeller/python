'''Character Reading Program by Naomi Keller. Version 1.2, last updated 4/12/2019.
This program determines how many of each type of character are in a text document.
VARIABLES:
fileObj = The import of text.txt
allText = String made from fileObj
numUpper/Lower/Digit/Wspc = Hold the amount of character types found by loop
'''
#opening file
fileObj = open('text.txt', 'r')

#making one large string from file
allText = fileObj.read()

#variables for holding totals of each type of character
numUpper = 0
numLower = 0
numDigit = 0
numWspc = 0

#loop for finding and adding characters to the variables
for ch in allText:
    if ch.isupper():
        numUpper += 1
    elif ch.islower():
        numLower += 1
    elif ch.isdigit():
        numDigit += 1
    elif ch.isspace():
        numWspc += 1

#output
print('Types of characters in Text: ')
print('Uppercase Letters: ', numUpper)
print('Lowercase Letters: ', numLower)
print('Digits: ', numDigit)
print('Spaces: ', numWspc)

    
