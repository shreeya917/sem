x=["a","b","c"]
print(x)
x.insert(4,"d")
print(x)
x.remove("a")
print(x)
y=[1,2]
x.extend(y)
print(x)
print(x[0:2])
print(x.index("c")) #for location

a=list(range(10))

print(a)
print(a[2])
print(a[2:])
print(a[:2])
print(a[2:6])
print(a[2:-2])
print(a[-6:-2])
print(a[:])
print(a[2::2])
print(a[:6:2])
print(a[2:6:2])
print(a[::-1])
print(a[::-2])
print(a[-6:-2:1])