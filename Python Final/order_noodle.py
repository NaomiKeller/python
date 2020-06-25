# Noodle Order Form
# By Naomi Keller
# Last edited: 4/19/2019
# This program displays the records in the
# noodle.txt file.

#View is a function that displays the record, taken from show_noodle
def view():
    try:
        # Open the noodle.txt file.
        noodle_file = open('noodle.txt', 'r')
    
        # Read the first record's description field.
        descr = noodle_file.readline()
    except IOError:
        print('IOError: Please ensure the file was properly created.')
    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = float(noodle_file.readline())
        pricepp = float(noodle_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        # Display the record.
        print('Description:', descr)
        print('Quantity:', qty)
        print('Price per Pound:', pricepp)
        print('==================')

        # Read the next description.
        descr = noodle_file.readline()

    # Close the file.
    noodle_file.close()
# Call the view function
view()

#This function is for the user to order
def order():
    menu = 'Y'
    while menu == 'Y' or menu == 'y':
        found = False

        # Get the search value.
        search = input('Enter the description of which noodle you would like to buy: ')
        
        # Open the noodle.txt file.
        noodle_file = open('noodle.txt', 'r')

        # Read the first record's description field.
        descr = noodle_file.readline()

        # Read the rest of the file.

        while descr != '':
            # Read the quantity field.
            qty = float(noodle_file.readline())
            pricepp = float(noodle_file.readline())

                # Strip the \n from the description.
            descr = descr.rstrip('\n')

                # Determine whether this record matches
                # the search value.
            try:
                if descr == search:
                        # User input of how much they want to buy.
                        buy = float(input('How many pounds would you like to buy? : '))
                        if buy > qty or buy < 0:
                            print('Error: That amount is not available in stock.')
                        else:
                            order = buy * pricepp
                            # It then calculates the cost and gives output.
                            print('You have place an order for: ')
                            print(buy, 'pounds of', search, 'noodles.')
                            print('Your total is: $', order)
                            print('==================')
                        menu = input("Enter 'Y' to place another order or anything else to quit: ")
                        # Set the found flag to True.
                        found = True
                    # Read the next description.
                descr = noodle_file.readline()
            except ValueError:
                print('ValueError: Non-numeric data found.')            
                    # Close the file.
        noodle_file.close()
        
            # If the search value was not found in the file
            # display a message.
        if not found:
            print('That item was not found in the file.')

        
# Call the order function.
order()


