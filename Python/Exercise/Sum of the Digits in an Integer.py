digits = input("Enter 4 digits : ")
first_digit = int(digits) // 1000
second_digits = int(digits) // 100 - first_digit * 10
third_digits = int(digits) % 100 // 10
fouth_digit = int(digits) % 10
summary = first_digit + second_digits + third_digits + fouth_digit
print("The sum of numbers = {}".format(summary))
