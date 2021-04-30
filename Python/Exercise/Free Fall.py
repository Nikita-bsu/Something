from math import sqrt

h = float(input("Enter the heights from which the object is dropped in meters : "))
initial_speed = 0
acceleration = 9.8

final_speed = sqrt(initial_speed + 2 * acceleration * h)
print('The final speed is {:.2f}'.format(final_speed))