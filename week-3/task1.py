print("Choose a shape:")
print("1 - Rectangle")
print("2 - Circle")
print("3 - Triangle")

choice = int(input())

if choice == 1:
    a = float(input("Enter length: "))
    b = float(input("Enter width: "))
    area = a * b
    print("Area =", area)

elif choice == 2:
    r = float(input("Enter radius: "))
    area = 3.14 * r * r
    print("Area =", area)

elif choice == 3:
    a = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = 0.5 * a * h
    print("Area =", area)

else:
    print("Wrong choice")
