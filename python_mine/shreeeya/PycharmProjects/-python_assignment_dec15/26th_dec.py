#arguments
def f(*args):
     for each in args:
        print(each)


def g(**key):
    for k,v in key.items():
       print("{}:{}".format(k,v))




f(1,2,3,4)
g(x=1,y=2, z=3)



def s(**kwargs):
    total=0
    for k,v in kwargs.items():
       # total+=v
     total+=kwargs.get(k)

     print(total)



s(x=5,y=10,z=25)

