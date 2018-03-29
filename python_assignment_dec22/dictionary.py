#Ask for a number (n) as an input from user. Using the use input (n), write a program to generate a dictionary that contains (i, i*i) where i is key and i*i is a value
# for numbers between the range 1 and n (both included). and then the program should print the dictionary.


def f(go):
    diction=dict()
    for i in go:
        diction.update({i:i*i})

    print(diction)



n=int(input("Enter the number: "))
a = list(range(0,n+1))
f(a)