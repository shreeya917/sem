x={
    "a":123,
    "p":True,
    456:[4,5,6]
}

x.update(
    {"a":789}
)
print(x)
print(x.pop(456))

x.update(
    {"q":False}
)
print(x)
print(x.get("q"))
del x["p"]
print(x)
print(x.keys())
print(x.values())
print(x.clear())


