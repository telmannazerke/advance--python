def right_triangle_area(a, b):
    return a*b/2

def rectangle_area(a, b):
    return a*b

# input
X = float(input("enter X: "))
Y = float(input("enter Y: "))
Z = float(input("enter Z: "))
T = float(input("enter T: "))
area = right_triangle_area(X, Y) + rectangle_area(Z, T)

print("area =", area)
