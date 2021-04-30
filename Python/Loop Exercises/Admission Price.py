BABY_PRICE = 0.00
CHILDREN_PRICE = 14.00
ADULT_PRICE = 23.00
SENIORS_PRICE = 18.00

BABY_LIMIT = 2
CHILD_LIMIT = 12
ADULT_LIMIT = 64

total = 0

line = input("Enter the age of the guest (blank to quit): ")

while line != "":
    age = int(line)

    if age <= BABY_LIMIT:
        total += BABY_PRICE
    elif BABY_LIMIT < age <= CHILD_LIMIT:
        total += CHILDREN_PRICE
    elif CHILD_LIMIT < age <= ADULT_LIMIT:
        total += ADULT_PRICE
    else:
        total += SENIORS_PRICE

    line = input("Enter the age of the guest (blank to quit): ")

print("Sum to the guest {:.2f}".format(total))