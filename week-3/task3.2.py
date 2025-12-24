s = input()

words = s.split()
result = []

for word in words:
    result.append("".join(sorted(word)))

print(" ".join(result))
