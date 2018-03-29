def divide(num):
    print(100/num)

try:
    #fp=open("dshj")
    #divide(0)
    divide(10)
except FileNotFoundError:
    print("File not found")
except ZeroDivisionError:
    print("Zero division not allowed")
#else:
    print("Success!!")
#finally:
    print("Code executes!!")




def print_hello():
        print("hello")

def print_world():
    print("world")


def default():
    print("Default")

switch={
    "1": print_hello(),
    "2": print_world()
}


try:
    switch[input("Enter the choice")]()
except KeyError:
    print("Default")