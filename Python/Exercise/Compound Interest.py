amount_of_money = float(input("Enter the amount of money that you want to contribute : "))


def balance(amount):
    balance_year1 = amount + (amount * 4) / 100
    balance_year2 = balance_year1 + (amount * 4) / 100
    balance_year3 = balance_year2 + (amount * 4) / 100

    print("Balance after the first year = {:.2f}$".format(balance_year1))
    print("Balance after the second year = {:.2f}$".format(balance_year2))
    print("Balance after the third year = {:.2f}$".format(balance_year3))


balance(amount_of_money)