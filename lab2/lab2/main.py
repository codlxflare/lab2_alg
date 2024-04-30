from brute_force_algorithm import *
from algorithm_on_the_map import *
from algorithm_on_the_tree import *

def modexp(x, y, N):
    if y == 0:
        return 1
    z = modexp(x, y // 2, N)
    if y % 2 == 0:
        return (z*z) % N
    else:
        return (x*z*z) % N

def generate_rectangles(n):
    rectangles = []
    i = 0
    while i < n:
        start = (10 * i, 10 * i)
        end = (10 * (2*n - i), 10 * (2*n - i))
        rectangle = Rectangle(start, end)
        rectangles.append(rectangle)
        i += 1.3
    return rectangles


def generate_points(n):
    points = []
    i = 0
    while i < n:
        point = (modexp(9973*i, 31, 20 * n), modexp(9967*i, 31, 20 * n))
        points.append(point)
        i += 1.3
    return points

def main():
    print("N|first|second_preparation second_search|third_preparation third_search")
    n = 10
    while n < 50000:
        print(f"{int(n)}|", end='')
        rectangles = generate_rectangles(n)
        points = generate_points(n)


        print(f"{int(first(rectangles, points))}|", end='')
        second_time = second(rectangles, points)
        print(f"{int(second_time[0])} {int(second_time[1])}|", end='')
        third_time = third(rectangles, points)
        print(f"{int(third_time[0])} {int(third_time[1])}", end='')
        print()
        n *= 1.5


if __name__ == "__main__":
    main()