''' (Triple quoted string ignored by program, used as multi-line comment)
Popular Name Search Program by Naomi Keller. Version 2.3, last updated 4/5/2019
This program uses two lists of popular names and allows a user to search a name to see if it is on the list.
VARIABLES:
girlFile / boyFile = used to import the external text files
girlName / boyName = holds each name iteratively from the list while the files are being read so that they can be appended and added to the internal list
girlList / boyList = the imported list from the external text files to be used in the program
allList = girlList and boyList combined for use in searching both lists
userMenu = user's input that determines which function to run
userName = user's input of a name to search
'''

# importing list of girl names in the program from file
girlFile = open("GirlNames.txt", "r")
girlName = girlFile.readline()
girlList = []

while girlName != "":
    girlName = girlName.rstrip ( "\n" )
    girlList.append(girlName)
    girlName = girlFile.readline()

girlFile.close()

# importing list of boy names in the program from file
boyFile = open("BoyNames.txt", "r")
boyName = boyFile.readline()
boyList = []

while boyName != "":
    boyName = boyName.rstrip ("\n" )
    boyList.append(boyName)
    boyName = boyFile.readline()

boyFile.close()

# combining the two list for if/when the user wants to search both lists
allList = boyList + girlList

# sees if the boys name is in the boys list
def boyFind():
    userName = input("Enter the boy name you would like to search (case sensitive): ")
    if str(userName) in boyList:
        print("The boys name", userName, "is among the popular names list!")
        #goes back to the menu
        menu()
    else: 
        print("The boys name", userName, "is not among the popular names list.")
        menu()

#sees if the girls name is in the girls list
def girlFind():
    userName = input("Enter the girl name you would like to search (case sensitive): ")
    if str(userName) in girlList:
        print("The girls name", userName, "is among the popular names list!")
        menu()
    else: 
        print("The girls name", userName, "is not among the popular names list.")
        menu()

#sees if the name is in either list
def bothFind():
    userName = input("Enter the name you would like to search (case sensitive): ")
    if str(userName) in girlList:
        print("The name", userName, "is among the popular names list!")
        menu()
    else: 
        print("The name", userName, "is not among the popular names list.")
        menu()

# user input
def menu():
    userMenu = input("Enter 'Boy' to search for a boys name, 'Girl' to search for a girls name, or 'Both' to search both. enter 'X' to quit: ")
    if userMenu == "Boy" or userMenu == "boy":
        boyFind()
    elif userMenu == "Girl" or userMenu == "girl":
        girlFind()
    elif userMenu == "both" or userMenu == "Both":
        bothFind()
    elif userMenu == "x" or userMenu == "X":
        print("Thank you for using the Popular Name Search Program. You may now close this window.")
        raise SystemExit

menu()
