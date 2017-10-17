# Python Object Oriented Programming


class Employee:
    """Practice class"""

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        """Find email format
        The @property decorator allows us to access the class method
        just like we would an attribute"""
        return '{}.{}'.format(self.first, self.last)

    @property
    def fullname(self):
        """Find full name format"""
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        """Allows us to alter the first, last names and email of employee"""
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        """Allows us to delete the first, last names and email of employee"""
        print("Delete Name!")
        self.first = None
        self.last = None
        
emp_1 = Employee('John', 'Smith')

emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname