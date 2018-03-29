class Person :
    def __init__(self ,fname,lname):
        self.fname =fname
        self.lname=  lname


    @property
    def email(self):
        return self.fname+"."+self.lname+"@company.com"



p=Person("First","Last")
print(p.email)
p.fname ="User"
print(p.email)



#greater secter


#classmethod
#property
#static method
#decorator