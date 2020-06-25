# Show Noodle Record
# By Naomi Keller
# Last edited: 4/19/2019
# This program displays the records in the
# noodle.txt file.

def main():
    # Open the noodle.txt file.
    try:
        noodle_file = open('noodle.txt', 'r')
    except IOError:
        print('IOError: Please ensure the file was properly created.')
    # Read the first record's description field.
    descr = noodle_file.readline()

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

# Call the main function.
main()


