import math


def hypotenuse(a, b):
    return math.sqrt(a*a + b*b)

a1 = float(input("Enter first leg of triangle 1: "))
b1 = float(input("Enter second leg of triangle 1: "))

a2 = float(input("Enter first leg of triangle 2: "))
b2 = float(input("Enter second leg of triangle 2: "))

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print("Hypotenuse 1 =", h1)
print("Hypotenuse 2 =", h2)

if h1 > h2:
    print("The first hypotenuse is greater")
elif h1 < h2:
    print("The second hypotenuse is greater")
else:
    print("The hypotenuses are equal")
