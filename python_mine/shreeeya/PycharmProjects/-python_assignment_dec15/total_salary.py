#Q1. The salary of employees in a software company is stored in a list, i.e. salary = [15000, 20000, 17000, 18900, 30000].
#  When annual review was conducted, accounting department made a decision to increase the salary of every employee by 23%.
# Now, write a pythonic code to find out how much is the total salary for each employee after the raise.

salary= [15000, 20000, 17000, 18900, 30000]

print("Initial Salary \t Increased Salary(23%)")
for s in salary:
    print(s,end="\t\t\t\t")
    s= s+(23*s/100)
    print(s)