'''
Create a Employee class and initialize it with first_name, last_name and salary.
Also, it has a derived attribute called email, which is self generated when instance is created.
     make methods to :
      a. Display - It should display all information of the employee instance.
'''


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


    def emailGenerator(self):
        self.email = self.fname.lower()+'.'+self.lname.lower()+'@deerwalk.edu.np'

    def displayInfo(self):
        print("First name: {}\nLast name: {}\nEmail: {}".format(self.fname, self.lname, self.email))


emp1 = Employee(input('Enter first name: '), input('Enter last name: '))
emp1.emailGenerator()
emp1.displayInfo()