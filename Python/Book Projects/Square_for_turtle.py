import turtle

bob = turtle.Turtle()


#
# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)


# print(square(bob, 100))

# def polygon(t, length, n):
#     for i in range(4):
#         t.fd(length)
#         t.lt(360 / n)
#
# print(polygon(bob, 100, 4))
def polygon(t, length, n):
    for i in range(4):
        t.fd(length * n)
        t.lt(360 / n)


def circle(t, r):
    polygon(t, r, 360)


print(circle(bob, 10))
