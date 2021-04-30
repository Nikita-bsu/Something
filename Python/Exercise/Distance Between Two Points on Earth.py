import math

t1 = float(input("Введите широту первой точки : "))
g1 = float(input("Введите долготу первой точки : "))

t2 = float(input("Введите широту второй точки : "))
g2 = float(input("Введите долготу второй точки : "))

tup1 = (t1, g1)
tup2 = (t2, g2)


def convert_degres(deg1):
     t = math.radians(deg1)
     return t


def dist(coor1, coor2):
    distance = 6371.01 * math.acos(math.sin(convert_degres(coor1[0])) *
                                   math.sin(convert_degres(coor2[0])) +
                                   math.cos(convert_degres(coor1[0])) *
                                   math.cos(convert_degres(coor2[0])) *
                                   math.cos(convert_degres(coor1[1]) - convert_degres(coor2[1])))
    return distance


print("The distance between {} and {} = {:.3f}".format(tup1, tup2, dist(tup1, tup2)))