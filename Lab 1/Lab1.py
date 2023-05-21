import math

def solve_quadratic_equation(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Уравнение имеет два действительных корня:", root1, root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        print("Уравнение имеет один действительный корень:", root)
    else:
        print("Уравнение не имеет действительных корней")


