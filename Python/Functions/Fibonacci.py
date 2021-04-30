# def fibonacci(item):
#     f1 = f2 = 1
#     while item > 2:
#         buff = f2
#         f2 = f1 + f2
#         f1 = buff
#         item -= 1
#     return f2
#
#
# n = int(input())
# m = fibonacci(n)
# print(m)


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

m = int(input())
print(fibonacci(m))