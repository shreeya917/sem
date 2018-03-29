class dog:
    sound="bark"
    legs=4
    def __init__(self,name):
        self.name=name

d1 = dog("TOM")
d2 = dog("Jerry")
print(d1.name,d1.sound, d1.legs)
dog.legs=3
print(d2.name,d2.sound,d2.legs)


class dogs:
    no_dogs=0
    def __init__(self):
        dogs.no_dogs +=1

d1= dogs()
print(d1.no_dogs)
d2 = dogs()
d3=dogs()
print(d1.no_dogs)