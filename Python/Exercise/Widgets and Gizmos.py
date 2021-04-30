widgets = int(input("Enter the number of widgets : "))
gizmos = int(input("Enter the number of gizmos : "))


def total(wid, giz):
    total_sum = (wid * 75) + (giz * 112)
    if total_sum >= 1000:
        kg = total_sum // 1000
        part = total_sum - kg*1000
        print("Total weight of the order is equal to {0} kg and {1} grams".format(kg, part))
    else:
        print("Total weights of the order is equal to {} grams".format(total_sum))


total(widgets, gizmos)