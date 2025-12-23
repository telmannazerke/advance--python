s = input("Your input: ")

count = 0
if len(s) < 5:
    print(count)
else:
    for i in range(len(s) - 4):
        if s[i:i+5] == ">>-->" or s[i:i+5] == "<--<<":
            count += 1

        print(count)








