print("choose a shape:")
print("1 - rectangle")
print("2 - circle")
print("3 - triangle")

choice = int(input())
if choice == 1:
    a = float(input("enter length: "))
    b = float(input("enter width: "))
    area = a*b
    print("area =", area)
elif choice == 2:
    r = float(input("enter radius: "))
    area = 3.14*r*r
    print("area =", area)
elif choice == 3:
    a = float(input("enter base: "))
    h = float(input("enter height: "))
    area = 0.5*a*h
    print("area =", area)
else:
    print("wrong choice")
