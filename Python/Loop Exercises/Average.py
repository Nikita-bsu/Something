count = 0
sum = 0
while True:
    a = int(input("Enter the number (the first number is not 0) : "))
    count += 1
    sum += a
    if a == 0:
        count -= 1
        average = sum / count
        print("Average = {}".format(average))
        break
