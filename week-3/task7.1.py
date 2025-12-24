def right_triangle_area(a, b):
    return a * b / 2

def rectangle_area(a, b):
    return a * b


# input
X = float(input("Enter X: "))
Y = float(input("Enter Y: "))
Z = float(input("Enter Z: "))
T = float(input("Enter T: "))

area = right_triangle_area(X, Y) + rectangle_area(Z, T)

print("Area of quadrilateral =", area)
