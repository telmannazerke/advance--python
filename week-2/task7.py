items = input().split()

counts = {}


for x in items:
    counts[x] = counts.get(x, 0) + 1

print("Purchase frequency:")
for x in counts:
    print(x + ":", counts[x])


most = max(counts, key=counts.get)
print("Most popular item:", most)


once = [x for x in counts if counts[x] == 1]
print("Purchased once:", " ".join(once))


sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)

print("Sorted by frequency:")
for x, c in sorted_items:
    print(x, c)
