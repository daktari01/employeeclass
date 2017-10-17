# Python Object Oriented Programming


class Employee:
    """Practice class"""

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        """Find full name fomat"""
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        """Find raise of salary"""
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    #Alternative class constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    """Class Developer inheriting from Employee class"""
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        '''Redefining the Employer init method to 
        include the prog_lang too'''
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    """Class Manager extends Employee"""
    def __init__(self, first, last, pay, employees = None):
        '''Redefining the Employer init method to 
        include the employees managed by manager'''
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        '''Method to define how employees are added to manager'''
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        '''Method to define how employees are removed from manager'''
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        '''Method to print employees managed by manager'''
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'JavaScript')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(isinstance(mgr_1, Manager))
print(issubclass(Developer, Employee))

'''print(dev_1.email)
print(dev_2.email)

print(dev_1.prog_lang)'''