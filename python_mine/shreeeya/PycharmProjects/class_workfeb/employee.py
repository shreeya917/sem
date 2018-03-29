


#class method
class Employee:
    no_of_emp=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.no_of_emp+=1

    def get_name(self):
        return self.name

    @classmethod
    def gen_emp_from_string(cls,inp):
        name,salary=inp.split("_")
        return cls(name,salary)


e = Employee.gen_emp_from_string("Sagar_2000")
print(e.__dict__)
