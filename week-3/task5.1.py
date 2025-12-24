def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))
D = int(input("Enter D: "))


num = A * D - C * B
den = B * D

g = gcd(abs(num), den)
num //= g
den //= g

print("Result:", num, "/", den)
