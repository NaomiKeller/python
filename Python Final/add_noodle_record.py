# Add Noodle Record
# By Naomi Keller
# Last edited: 4/19/2019
# This program adds noodle inventory records to
# the noodle.txt file.

def main():
    # Create a variable to control the loop.
    another = 'y'

    # Open the noodle.txt file in append mode.
    noodle_file = open('noodle.txt', 'a')

    # Add records to the file.
    while another == 'y' or another == 'Y':
        # Get the noodle record data.
        try:
            print('Enter the following noodle data:')
            descr = input('Description: ')
            qty = int(input('Quantity (in pounds): '))
            pricepp = float(input('Price per pound: '))
        
            # Append the data to the file.
            noodle_file.write(descr + '\n')
            noodle_file.write(str(qty) + '\n')
            noodle_file.write(str(pricepp) + '\n')
    
            # Determine whether the user wants to add
            # another record to the file.
            print('Do you want to add another record?')
            another = input('Y = yes, anything else = no: ')
        except IOError:
            print('IOError: Please ensure the file was properly created.')
        except ValueError:
            print('ValueError: Non-numeric data found.')

    # Close the file.
    noodle_file.close()
    print('Data appended to noodle.txt.')

# Call the main function.
main()

        
