a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))


def median(num1, num2, num3):
    return num1 + num2 + num3 - min(num1, num2, num3) - max(num1, num2, num3)


print(median(a, b, c))