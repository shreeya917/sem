my_str=[]
print(dir(my_str))
#dunder


class MyFirstclass:
    """This is documentation"""

    pass
a=MyFirstclass()
b=MyFirstclass()
#print(a.__doc__)
print(dir(a))
#print(dir(object))



class Point:
    pass
p1=Point()
p2=Point()

p1.x=5
p1.y=4

p2.x=3
p2.y=6

print(p1.x,p2.y)
print(p2.x,p1.y)


class pt:
    def reset(self):
        self.x=0
        self.y = 0


 #p=pt()
#p.x=5
#p.y=4
#pt.reset(p)
#p.reset()


class Student:
    def __init__(self,name,semester):
        self.name=name
        self.semester=semester

    def reset(self):
        self.semester+=1

s=Student('abc',1)

s.reset()
print(s.name,s.semester)






