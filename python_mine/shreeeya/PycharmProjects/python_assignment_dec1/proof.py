#Prove tha (a + b)^2 = a^2 + 2*a*b + b^2
from math import *

a = input("enter value of a :")
a = int(a)
b = input("enter value of b :")
b = int(b)


def lhs(a, b):
    return (a + b) ** 2


def rhs(a, b):
    return a ** 2 + 2 * a * b + b ** 2


c = lhs(a, b)
d = rhs(a, b)

if c == d:
    print("since LHS = {0} and RHS = {1} So the given expression is correct".format(c,d))
