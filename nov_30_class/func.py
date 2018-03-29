def LHS(a,b):
    return (a+b)**2

def RHS(a,b):
    return a**2+2*a*b+b**2

num1=int(input("Enter the value for a:"))
num2=int(input("Enter the value for b:"))

L=LHS(num1,num2)
R=RHS(num1,num2)

print("{}={}".format(L,R))

print("Therefore,(a+b)^2=a^2+2ab+b^2, proved")