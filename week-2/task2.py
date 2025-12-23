a = input()
b = input()

m = len(b)
bb = b + b

count = 0

for i in range(len(a) - m + 1):
    if a[i:i+m] in bb:
        count += 1

print(count)
