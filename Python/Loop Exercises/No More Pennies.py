PENNIS_PER_NICKEL = 5
NICKEL = 0.05

total = 0.0

line = input("Enter the price of the item (blank to quit): ")

while line != "":
    total += float(line)
    line = input("Enter the price of the item (blank to quit): ")
print("The exact amount payable is {:.2f}".format(total))

rounding_indicator = total * 100 % PENNIS_PER_NICKEL
if rounding_indicator < PENNIS_PER_NICKEL / 2:
    cash_total = total - rounding_indicator / 100
else:
    cash_total = total + NICKEL - rounding_indicator / 100

print("The cash amount payable in {:.2f}".format(cash_total))