n, m = map(int, input().split())
s = input().strip()

uniq = set()

for i in range(n - m + 1):
    uniq.add(s[i:i+m])

print(len(uniq))
