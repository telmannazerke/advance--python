def inside_circle(x, y, a, b, r):
    if (x - a)**2 + (y - b)**2 < r**2:
        return True
    else:
        return False
    
a = float(input("enter center x: "))
b = float(input("enter center y: "))
r = float(input("enter radius: "))

count = 0
for i in range(3):
    x = float(input("enter x of point: "))
    y = float(input("enter y of point: "))

    if inside_circle(x, y, a, b, r):
        count += 1

print("points inside the circle:", count)
