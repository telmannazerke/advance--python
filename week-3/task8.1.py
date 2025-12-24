n = int(input("Enter n: "))

for x in range(1, n + 1):
    ok = True
    temp = x

    while temp > 0:
        digit = temp % 10
        temp //= 10

        if digit == 0 or x % digit != 0:
            ok = False
            break

    if ok:
        print(x, end=" ")
