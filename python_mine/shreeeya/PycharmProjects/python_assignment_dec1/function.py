def f(x):
    if(x>0):
        print("{} is greater than zero".format(x))
    elif(x<0):
        print("{} is less than zero".format(x))
    else:
        print("{} is equal to zero".format(x))


num=int(input("Enter the number:"))
f(num)
