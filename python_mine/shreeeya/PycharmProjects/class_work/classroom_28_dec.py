div=lambda x,y:x/y
print(div(5,2))


di=lambda x,y: x/y if y>0 else 'div not possible'
print(di(2, 0))



x=[1,2,3,4]
x_new=list()
def square(i):
    return i**2

for each in x :
    x_new.append(square(each))
print(x_new)

y=[2,4,6,8,10]
y_new=map(lambda n:n**2,y)
print(list(y_new))

l=["hello","world","hola"]
print(list(filter(lambda x:x.startswith("h"),l )))
