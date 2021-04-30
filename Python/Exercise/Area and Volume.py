import math

radius = float(input("Enter the radius : "))

area_circle = math.pi * (radius ** 2)
volume_sphere = (4/3) * math.pi * (radius ** 3)

print("The area of a circle is {0:.3f}, the volume of a sphere is {1:.3f}".format(area_circle, volume_sphere))
