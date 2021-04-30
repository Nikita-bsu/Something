from math import sqrt

a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))
c = float(input("Enter the third number : "))

descriminante = sqrt(b ** 2 - 4 * a * c)

if descriminante < 0:
    print("The equation {0}x^2+{1}x+{2} = 0 hasn't real roots".format(a, b, c))
elif descriminante == 0:
    root = -b / (2*a)
    print("It has one real root = {0}".format(root))
else:
    root1 = (-b + descriminante) / (2*a)
    root2 = (-b - descriminante) / (2*a)
    print("It has two real roots = {0:.3f}, {1:.3f}".format(root1, root2))