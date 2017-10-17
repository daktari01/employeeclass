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

    def __repr__(self):
        '''Returning a string that can be used to recreate an object
        Mostly used by fellow developers'''
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        '''Meant to be more readable for the end user
        These two methods allow us to change how our objects are printed
        and dispalyed'''
        return '{} - {}'.format(self.fullname(), self.email)
        
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1)

repr(emp_1)
str(emp_1)

'''Dunder methods can also be used to perform arithmetic calculation'''
print(1 + 2)
print(int.__add__(1,2))
print(str.__add__('a', 'b')) #string __add__ concatenates the strings