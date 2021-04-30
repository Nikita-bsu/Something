from math import sqrt

first_side = float(input("Enter the first side: "))
second_side = float(input("Enter the second side: "))


def hypotenuse(cathetus1, cathetus2):
    hypotenuses = sqrt(cathetus1 ** 2 + cathetus2 ** 2)
    return hypotenuses


print("The hypotenuses of the right triangle = {:.2f}".format(hypotenuse(first_side, second_side)))