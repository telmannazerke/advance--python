a = float(input("First number: "))
operation = input("Operation: ")
b = float(input("Second number: "))

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    if b != 0:
        result = a / b
    else:
        print("Error: division by zero")
        exit()
else:
    print("Invalid operation")
    exit()

print(a, operation, b, "=", result)