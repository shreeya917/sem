def f(num):
    total=2*num+3
    print("2*{}+3={}".format(num,total))

f(3)
def greeting(style='-'):
		print(style*29)
		print("  Hello world  ")
		print(style*29)
greeting()
greeting("*")
greeting(style="=")


num1=2
num2=4
appx_pi=22/7
print("{0}+{1}*{0}={2}".format(num1,num2,num1+num2*num1))
print("{0:.2f}".format(appx_pi))
print("{0:.3f}".format(appx_pi))
print("{0:<10.3f} and 5.12".format(appx_pi))
print("{0:>10.3f} and 5.12".format(appx_pi))

x=range(1,10)
for each in x:
	print(each)

for each in range(1,10,2):
	print(each)
