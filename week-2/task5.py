allowed = "ABCEHKMOPTXY"

n = int(input())

for _ in range(n):
    s = input()

    if len(s) != 6:
        print("No")
        continue

    if s[0] not in allowed:
        print("No")
        continue

    if not (s[1].isdigit() and s[2].isdigit() and s[3].isdigit()):
        print("No")
        continue

    if s[4] not in allowed or s[5] not in allowed:
        print("No")
        continue

    print("Yes")

