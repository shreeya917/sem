#Define a global static password value by yourself. Then define a function which prompts user for a password.
# If the password is a match, print "password match" or else print "Wrong password"

def f(check):
    correct_pw= "123456"
    if check==correct_pw:
        print("PASSWORD MATCH!")
    else:
        print("WRONG PASSWORD")
    print("-"*20)

user= str(input("USERNAME: "))
password= str(input("PASSWORD: "))
f(password)

x=['a','b']
print("*".join(x))

z="python"
x.reverse()
print(reversed(z))
