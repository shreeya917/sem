#comprehension


my_list=list(range(0,10))
print("my_list=",my_list)

my_cube=[n*n*n for n in my_list]
print("my_cube=",my_cube)
#sqrt


def print_hello():
    print("hello")

x=print_hello
#value print(x)
x()


def squared(x):
    return x*x

print("function:",squared(5))

sq=lambda x: x*x
print("lambda:",sq(6))

l=lambda x:[n*n for n in x]
print(l([1,2,3]))

maximum=lambda x,y: x if x>y else y
print(maximum(3,123))


def squared(x):
    return x*x
l=[1,2,3,4]
F=map(squared,l)
print(list(F))

n=[1,2,3,4]
print(list(map(lambda x:x*x,n)))
print(list(filter(lambda x: x>2,n)))

#odd value
s=list(range(0,10))
print(list(map(lambda x,y: x %2==0 else s)))

