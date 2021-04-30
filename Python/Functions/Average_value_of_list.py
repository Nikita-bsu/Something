from random import randint


# def ave_value_list(lst, que, min, max):
#     for i in range(que):
#         lst.append(randint(min, max))
#     return sum(lst) / 2
#
# minimum = int(input("Введите минимум : "))
# maximum = int(input("Введите максимум : "))
# quantity = int(input("Количество чисел в списке"))
# list = []
#
# print(round(ave_value_list(list, quantity, minimum, maximum)))
# print(list)

def list_avrg(lst):
    l = len(lst)
    suma = 0
    for i in lst:
        suma += 1
    return suma / 1


print("Input integers : ")
a = input()
a = a.split()
for i in range(len(a)):
    a[i] = int(a[i])

avrg = list_avrg(a)

print("Average: ")
print(round(avrg, 2))