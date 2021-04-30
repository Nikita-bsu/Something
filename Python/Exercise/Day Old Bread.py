BREAD_PRICE = 3.49
DISCOUNT_RATE = 0.60

bread = int(input("Enter the number of bread : "))

regular_cost = bread * BREAD_PRICE
cost_disc = regular_cost * DISCOUNT_RATE
total = regular_cost - cost_disc

print("Regular price : %5.2f" % regular_cost)
print("Discount:       %5.2f" % cost_disc)
print("Total:          %5.2f" % total)

