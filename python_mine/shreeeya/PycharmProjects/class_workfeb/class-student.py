class Student:
    def __init__(self ,name,semester):
        self.name= name
        self.semester = semester



    def get_name(self):
        return self.name


    @classmethod
    def get_obj_from_string(cls,inp):
        name , semester = inp.split("-")
        return cls(name,semester)


s1=Student.get_obj_from_string("Test-3")
print (s1.__dict__)



