x=[3,4,1,"a","b"]
index=x.index("a")
print(index)
y=["p","q"]
x.extend(y)
print(x)
pop=x.pop()
print(pop)
x.append()


x=[3,4,1,"a","b"]
a=x.index("a")
print(a)

y=["p","q"]
a=x.extend(y)
print(x)

a=x.append("xyz")
print(x)

c=x.remove(1)
print(x)



a=x.sort()
print(x)

b=x.sort(reverse=true)
print(x)


x=[3,4,1,"a","b"]
a=x.pop()
print(a)
print(x)