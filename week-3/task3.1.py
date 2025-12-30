import math


def hypotenuse(a, b):
    return math.sqrt(a*a+b*b)

a1 = float(input("enter first leg of triangle 1: "))
b1 = float(input("enter second leg of triangle 1: "))

a2 = float(input("enter first leg of triangle 2: "))
b2 = float(input("enter second leg of triangle 2: "))

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print("hypotenuse 1 =", h1)
print("hypotenuse 2 =", h2)

if h1 > h2:
    print("the first hypotenuse is greater")
elif h1 < h2:
    print("the second hypotenuse is greater")
else:
    print("the hypotenuses are equal")
