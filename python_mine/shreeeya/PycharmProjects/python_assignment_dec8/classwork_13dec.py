list=[]
list2=[5, 10 ,8, 9 ,56, 20, 21]

list.extend(list2)
print(list)


list.sort()
print(list)


list.sort(reverse=False)
print(list)


c=[5,24,3]
print("MAX: ", max(c))
print("MIN: ", min(c))
print(50 not in c)

w=["OOP", "CSA", "NM", "MGMT", "OS"]
joined = "**".join(w)
print(joined)


#Given a string "Python" generate output as :"nohtyp"
#Given a string " I love Python PL",extract the sting "Python" (use slicing)
#Given a string "a+b+c+d", generate a list from it.


x = ["Python"]
print(x[6:1:-1])

s=  "IlovePythonPL"
print(s[5:11])

z="a+b+c+d"
list_plus = z.split("+")
print(list_plus)