def inside_circle(x, y, a, b, R):
    if (x - a)**2 + (y - b)**2 < R**2:
        return True
    else:
        return False


a = float(input("Enter center x: "))
b = float(input("Enter center y: "))
R = float(input("Enter radius: "))

count = 0

for i in range(3):
    x = float(input("Enter x of point: "))
    y = float(input("Enter y of point: "))

    if inside_circle(x, y, a, b, R):
        count += 1

print("Points inside the circle:", count)
