'''
Weekly Sales Program by Naomi Keller. Version 1.1, last updated 4/5/2019.
This program asks for total sales per day of a week and totals them for the whole week.
'''
total = 0
#user input
mon = int(input("Enter the total sales for Monday: "))
tue = int(input("Enter the total sales for Tuesday: "))
wed = int(input("Enter the total sales for Wednesday: "))
thu = int(input("Enter the total sales for Thursday: "))
fri = int(input("Enter the total sales for Friday: "))
sat = int(input("Enter the total sales for Saturday: "))
sun = int(input("Enter the total sales for Sunday: "))
#input variables then stored in list
week = [mon, tue, wed, thu, fri, sat, sun]
#adds together each day in 'week'
for storeSales in week:
    total += storeSales
#output
print("Total sales for the week: $ %.2f" % total)
