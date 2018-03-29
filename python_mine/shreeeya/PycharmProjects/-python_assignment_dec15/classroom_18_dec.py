subject={
    "name": "Python",
    "type": "Extra credit",
    "hasExam" : "True",
    "midterm": 40,
    "Finalterm": 80,
    "grade system": ["A+", "A","B","C"],
    ("Assignment",): "Once a week",

}

print("dictionary items=", subject)
print("length=",len(subject))
print(subject["name"])
print(subject["hasExam"])


work={
    "abc": 123,
    "Hello": True,
}

work.update(
    {"abc":[1,2,3],"Hello":False,"world":True}
)
print(work)

print(work.get("world"))
print(work.get("xyz","xyz is not in dictionary"))




