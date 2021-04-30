n = int(input("Введите целое число : "))


def sumn(integer):
    sum = (integer * (integer + 1)) // 2
    return int(sum)


print("Сумма от 1 до {0} = {1}".format(n, sumn(n)))
