class Person:
    pass

p= Person()

class Animal:
    def eat(self):
        print("Eat method")

a= Animal()
a.eat()
print(a.__dict__)

a.name="Dog"
print(a.__dict__)