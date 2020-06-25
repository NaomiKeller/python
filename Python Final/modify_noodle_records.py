# Modify Noodle Record
# By Naomi Keller
# Last edited: 4/19/2019
# This program allows the user to modify the quantity
# in a record in the noodle.txt file.

import os  # Needed for the remove and rename functions

def main():
    # Create a bool variable to use as a flag.
    found = False
    try:
        # Get the search value and the new quantity.
        search = input('Enter a description to search for: ')
        new_qty = int(input('Enter the new quantity: '))
        new_pricepp = float(input('Enter the price per pound: '))
        
        # Open the original noodle.txt file.
        noodle_file = open('noodle.txt', 'r')
        
        # Open the temporary file.
        temp_file = open('temp.txt', 'w')
        
        # Read the first record's description field.
        descr = noodle_file.readline()
    except ValueError:
        print('ValueError: Non-numeric data found.')
    except IOError:
        print('IOError: Please ensure the file was properly created.')
    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = float(noodle_file.readline())
        pricepp = float(noodle_file.readline())
    
        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        # Write either this record to the temporary file,
        # or the new record if this is the one that is
        # to be modified.
        if descr == search:
            # Write the modified record to the temp file.
            temp_file.write(descr + '\n')
            temp_file.write(str(new_qty) + '\n')
            temp_file.write(str(new_pricepp)+ '\n')
            # Set the found flag to True.
            found = True
        else:
            # Write the original record to the temp file.
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')
            temp_file.write(str(pricepp) + '\n')
        # Read the next description.
        descr = noodle_file.readline()

    # Close the noodle file and the temporary file.
    noodle_file.close()
    temp_file.close()

    # Delete the original noodle.txt file.
    os.remove('noodle.txt')

    # Rename the temporary file.
    os.rename('temp.txt', 'noodle.txt')

    # If the search value was not found in the file
    # display a message.
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

# Call the main function.
main()
