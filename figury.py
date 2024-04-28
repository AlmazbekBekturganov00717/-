import math
def discr(a, b, c):
    D = (b ** 2) - 4 * a * c
    print(D)
    if D > 0:
        x_1 = (-b + math.sqrt(D)) / 2 * a
        x_2 = (-b - math.sqrt(D)) / 2 * a
        print(x_1, x_2)
    else:
        print("Корней нету")

discr(3 , 10, 3)