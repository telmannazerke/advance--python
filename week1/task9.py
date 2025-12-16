ticket = input()

sum_first = 0
sum_last = 0

for i in range(3):
    sum_first += int(ticket[i])
    sum_last += int(ticket[i + 3])

print("YES" if sum_first == sum_last else "NO")
