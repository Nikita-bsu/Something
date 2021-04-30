from math import sqrt

x_coor = float(input("Enter the x coordinate: "))
y_coor = float(input("Enter the y coordinate: "))

perimeter = 0

x_prev = x_coor
y_prev = y_coor

line = input("Enter the x coordinate (blank to quit): ")

while line != "":
    x = float(line)
    y = float(input("Enter the y coordinate: "))

    dist = sqrt((x_prev - x)**2 + (y_prev - y)**2)
    perimeter += dist

    x_prev = x
    y_prev = y

    line = input("Enter the x coordinate (blank to quit): ")

dist = sqrt((x_coor - x)**2 + (y_coor - y)**2)
perimeter += dist

print("The perimeter of the polygon is {0:.2f}".format(perimeter))