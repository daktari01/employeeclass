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

    def __add__(self, other):
        '''When we add two employees together, it will give us combined pay'''
        return self.pay + other.pay

    def __len__(self):
        '''Returns number of characters in employee,s name'''
        return len(self.fullname())
        
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1 + emp_2)
print(len(emp_1))
