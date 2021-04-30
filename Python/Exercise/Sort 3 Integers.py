a = int(input("Enter the first integer : "))
b = int(input("Enter the second integer : "))
c = int(input("Enter the third integer : "))

maximum = max(a, b, c)
minimum = min(a, b, c)
middle = (a+b+c) - maximum - minimum

print("Maximum = {0}, minimum = {1}, middle = {2}".format(maximum, minimum, middle))