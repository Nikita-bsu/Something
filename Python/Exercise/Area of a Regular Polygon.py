from math import pi, tan

n = int(input("The number of sides : "))
s = float(input("The length of a side : "))

area = (n * s ** 2) / (4 * tan(pi / n))
print("The area of a regular polygon is {:.3f}".format(area))