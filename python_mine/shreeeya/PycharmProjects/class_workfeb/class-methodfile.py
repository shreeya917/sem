class Student:
    def __init__(self,name,sem):
      self.name=name
      self.sem=sem

@classmethod
def gen_emp_from_string(cls,inp):
    name,sem=inp.split("-")
    return  cls(name,sem)


students=[]
with open ('data.txt','r') as fp:
    for each in fp:
     students.append(Student.gen_emp_from_string(each))
print (len(students))



stud={}
with open ('E:\python\data.txt','r') as fp:
    for index, each in enumerate(fp,start=1):
     stud.update({index:Student.gen_emp_from_string(each)})
print (stud)