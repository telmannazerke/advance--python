def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("enter A: "))
b = int(input("enter B: "))
g = gcd(a, b)
l = (a*b) // g

print("GCD =", g)
print("LCM =", l)
