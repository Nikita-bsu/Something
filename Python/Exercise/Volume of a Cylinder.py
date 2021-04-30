import math

radius = float(input("Enter the radius of a cylinder : "))
heights = float(input("Enter the heights of a cylinder : "))

volume = math.pi * (radius ** 2) * heights

print("The volume of the Cylinder equals {}".format(volume))