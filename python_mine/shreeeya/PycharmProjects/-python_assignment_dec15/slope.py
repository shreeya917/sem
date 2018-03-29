#Q4.  Function that solves the equation, y=mx+c where different values of x'es are [1, 2.3, 5.6, 7, 78].
#  Function shouldn't return any values but must print the value of y for each iteration.
#  Value of y should be in 2 decimal format. (m = 45, c = 0.5)

def f(value_x):
    m = 45
    c = 0.5
    for x in value_x:
        y = m*x + c
        print("{0:.2f}".format(y))


x_values = [1, 2.3, 5.6, 7, 78]
f(x_values)