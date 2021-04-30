FIRST_ITEM = 10.95
ANOTHER_ITEMS = 2.95


num_goods = int(input("Enter the number of goods you bought: "))


def cost(number_g):
    another_items = (number_g - 1) * 2.95
    return another_items + 10.95


print("You bought {0} items, so you need to pay {1}".format(num_goods, cost(num_goods)))
