# Importing classes from emp.py

from emp import Employee, ProductionWorker

# main function

def main():
    # Input, passing into classes to be stored
    worker = ProductionWorker(
        input('Enter employee name: '),
        int(input('Enter employee Number: ')),
        int(input('Enter employee shift Number: ')),
        float(input("Enter employee's Hourly Pay: " )))
    
    
    # Output
    print('========================================')
    print('= Confirmation of Employee Information =')
    print('========================================')
    print('Name:', worker.get_name())
    print('Employee Number:', worker.get_employee_number())
    print('Shift:', worker.get_shift().title())
    print('Hourly pay: $' + worker.get_hourly_pay())
    
main()