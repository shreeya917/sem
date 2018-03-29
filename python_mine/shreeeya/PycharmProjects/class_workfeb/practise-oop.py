def funct(num):

 exp=num * 2 + num*2
 print(exp)

funct(3)




class Vampire:
  food = "HumanBlood"
eyecolor = "Red"
def __init__(self, name, superpower):
 self.name= name
 self.superpower = superpower

def get_info(self):
  return "{} - {} .".format(self.name,self.superpower)

v1 = Vampire("Edward", "Mind Reader")
v1.eyecolor = "Honey Gold"
v1.food = "Mountain Lion"
v2 = Vampire("Bella","Shield")
v2.food = "Mountain Lion"
v3 = Vampire("Aro","Mind Read with touch")

print(v1.get_info(),v1.food, v1.eyecolor)
print(v2.get_info(),v2.food, v2.eyecolor)
print(v3.get_info(),v3.food, v3.eyecolor)

class Employee:
 no_of_employee = 0
def __init__(self):
       Employee.no_of_employee +=1

print(Employee.no_of_employee)
e1 = Employee()
print(e1.no_of_employee)
e2 = Employee()
e3 = Employee()
print(e1.no_of_employee)
print(Employee.no_of_employee)

class ThirdS:
 semester = 3
eyecolor = "brown"

def __init__(self, name, roll):
  self.name= name
  self.roll = roll
def get_info(self):
 return "{} - {} .".format(self.name,self.roll)

s1 = ThirdS("Isha","624")

print(s1.get_info(),s1.semester)



class Student:
 def __init__(self, name, semester):
   self.name = name
   self.semester = semester

def updatesemester(self):
 self.semester +=1


b = Student("Sunita", 2)
print(b.name, b.semester)
Student.updatesemester(b)
print(b.name, b.semester)