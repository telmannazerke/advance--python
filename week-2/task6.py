def all_eq(lst):
    max_len = len(lst[0])
    for s in lst:
        if len(s) > max_len:
            max_len = len(s)

    result = []
    for s in lst:
        result.append(s + "_" * (max_len - len(s)))

    return result



n = int(input())      
words = []

for _ in range(n):
    words.append(input())


answer = all_eq(words)


for s in answer:
    print(s)
