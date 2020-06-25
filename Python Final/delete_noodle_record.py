# Delete Noodle Record
# By Naomi Keller
# Last edited: 4/19/2019
# This program allows the user to delete
# a record in the noodle.txt file.

import os  # Needed for the remove and rename functions

def main():
    # Create a bool variable to use as a flag.
    found = False

    # Get the noodle to delete.
    search = input('Which noodle do you want to delete? ')
    try:
        # Open the original noodle.txt file.
        noodle_file = open('noodle.txt', 'r')
    
        # Open the temporary file.
        temp_file = open('temp.txt', 'w')
    
        # Read the first record's description field.
        descr = noodle_file.readline()
    except IOError:
        print('IOError: Please ensure the file was properly created.')
    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = str(noodle_file.readline())
        pricepp = str(noodle_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        # If this is not the record to delete, then
        # write it to the temporary file.
        if descr != search:
            # Write the record to the temp file.
            temp_file.write(descr + '\n')
            temp_file.write(str(qty))
            temp_file.write(str(pricepp))
        else:
            # Set the found flag to True.
            found = True

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
