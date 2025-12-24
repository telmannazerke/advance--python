
def triangle_area(a, h):
    return 0.5 * a * h



a = float(input("Enter side of hexagon: "))


h = (3 ** 0.5) / 2 * a

hexagon_area = 6 * triangle_area(a, h)

print("Hexagon area =", hexagon_area)
