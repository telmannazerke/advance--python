import math

def heron(x,y,z):
    p = (x+y+z) / 2
    return math.sqrt(p*(p - x)*(p - y)*(p - z))

a = float(input("enter side a: "))
b = float(input("enter side b: "))
c = float(input("enter side c: "))
d = float(input("enter side d: "))
e = float(input("enter diagonal e: "))

area = heron(a,b,e) + heron(c,d,e)

print("area =", area)
