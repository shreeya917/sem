#Define a function to determine whether the user's integer input is a even number or an odd number.

def f(check):
    cond=check%2
    if cond==0:
        print("{}is an even number.".format(check))
    else:
        print("{}is an odd number.".format(check))

num=int(input("Enter number: "))
f(num)