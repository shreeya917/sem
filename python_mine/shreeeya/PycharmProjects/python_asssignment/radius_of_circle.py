#2. A Program to find the area of a circle

from math import pi

radius = float(input("Enter the Radius"))

area = pi*radius**2

print("{}*{}**2 = " .format (pi, radius),end="")
print("{0:.3f}".format(area))
