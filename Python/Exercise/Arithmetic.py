import math

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))


def arithmetic(int1, int2):
    sum = int1 + int2
    print("The sum of {0} + {1} = {2}".format(int1, int2, sum))

    different = int1 - int2
    print("The different when {0} is subtracted from {1} = {2}".format(int1, int2, different))

    product = int1 * int2
    print("The product of {0} * {1} = {2}".format(int1, int2, product))

    quotient = int1 // int2
    print("The quotient when {0} is divided by {1} = {2}".format(int1, int2, quotient))

    remainder = int1 % int2
    print("The remainder when {0} is divided by {1} = {2}".format(int1, int2, remainder))

    log = math.log10(int1)
    print("The result of log10 = {}".format(log))

    power = pow(int1, int2)
    print("The result of {0}^{1} = {2}".format(int1, int2, power))


arithmetic(a, b)