tup=tuple()
print(tup)
tup+=(3,4,"a")
print(tup)
pos=tup.index(4)
print(pos)

s=set()
s.update([3,4,9,"x"])
print(s)

p={4,9}
print(p.issubset(s))
p.clear()
print(p)


a=((),)
b=(3,4,'a')
a+=b
print(a)

c=a.index(4)
print(c)

s=set()
type(s)

d=(3,4,9,"x")
s.update(d)
print(d)

m=set()
p=(4,9)
m.update(p)
print(m)

m.issubset(s)
print(m)

s.clear()
print()