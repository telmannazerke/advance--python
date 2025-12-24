import math

def heron(x, y, z):
    p = (x + y + z) / 2
    return math.sqrt(p * (p - x) * (p - y) * (p - z))

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
d = float(input("Enter side d: "))
e = float(input("Enter diagonal e: "))

area = heron(a, b, e) + heron(c, d, e)

print("Area =", area)
