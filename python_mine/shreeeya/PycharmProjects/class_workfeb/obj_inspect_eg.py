print (dir(object))


class Person:
    pass
p= Person()
print(isinstance(1,int))
print(isinstance(1,float))
print(isinstance("a",str))
print(isinstance(p,Person))
print(isinstance(p,object))


#class Superhero:

print(1+2)
print("a"+"b")




class Employee:
    #test= None
    def __init__(self,name,salary):
        self.name=name
        self.salary = salary

        #def get_name(self):
        def __(self):
            #return self.name
            return "Employee({},{})".format(self.name, self.salary)

    def __str__(self):
        return  self.name

p= Employee("test",5000)
#print(dir(p))
#print(dir(perso))
#print(p.__str__())
#print(str(p))
#print(type(p))
#print(type(perso))
print(p)
p2= Employee("test2",4000)
print(p2)