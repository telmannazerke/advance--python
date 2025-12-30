def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

A = int(input("enter A: "))
B = int(input("enter B: "))
C = int(input("enter C: "))
D = int(input("enter D: "))

num = A*D
den = B*C

g = gcd(num, den)
num //= g
den //= g

print("result:", num, "/", den)
