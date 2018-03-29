# Function that prompts user to input his/her full name.
#After user enter's his/her full name, split it and store it in variables first_name and last_name.

count=0
k=0
name=str(input("Enter your full name: "))

for i in range(0,len(name)):
   if name[i]==' ':
       count+=1
       if count>1:
           middle_name=name[k:i]
           k=i+1
           print("The middle name is:",middle_name)
       else:
           k = i+1
           first_name=name[0:i]
           print("The first name is:",first_name)

last_name=name[k:len(name)]
print("The last name is:", last_name)