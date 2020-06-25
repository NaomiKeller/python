class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__employee_num = number
    
    #Mutators for empoyee class
    def set_name(self, name):
        self.__name = name
        
    def set_employee_number(self, number):
        self.__employee_num = number
        
    #Accessors for class
    def get_name(self):
        return self.__name
    
    def get_employee_number(self):
        return self.__employee_num
    
class ProductionWorker(Employee):
    def __init__(self, name, number, shift_num, hourly_pay):
        if shift_num == 1 or shift_num == 2:
            self.__shift = shift_num
        else:
            raise ValueError('The shift numbers are 1 for day and 2 for night')
        self.__hourly_pay = float(hourly_pay)
        Employee.__init__(self, name, number)
    # Mutators for ProductionWorker class
    def set_shift_number(self, shift_num):
        if shift_num == 1 or shift_num == 2:
            self.__shift = shift_num
        else:
            raise ValueError('The shift numbers are 1 for day and 2 for night')
    
    def set_hourly_pay(self, hourly_pay):
        self.__hourly_pay = float(hourly_pay)
        
    # Accessors for class
    
    def get_shift(self):
        if self.__shift == 1:
            return 'day'
        else:
            return 'night'
        
    def get_hourly_pay(self):
        return format(self.__hourly_pay, ',.2f')
