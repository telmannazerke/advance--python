n = int(input("Enter a non-negative integer: "))

octal = oct(n)[2:]

octal = octal.zfill(10)

print(octal)
