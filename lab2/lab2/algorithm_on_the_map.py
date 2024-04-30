import time

from bisect import bisect_right

class Rectangle:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __getitem__(self, key):
        if key == 0:
            return self.start
        elif key == 1:
            return self.end
        else:
            raise IndexError("Rectangle indices must be 0 or 1")

def second(rectangles, points):
    t0 = time.time()
    x_set = set()
    y_set = set()
    for r in rectangles:
        x_set.add(r.start[0])
        x_set.add(r.end[0])
        y_set.add(r.start[1])
        y_set.add(r.end[1])


    x = sorted(x_set)
    y = sorted(y_set)


    matrix = [[0] * len(y) for i in range(len(x))]


    for r in rectangles:
        x_start = bisect_right(x, r.start[0]) - 1
        x_end = bisect_right(x, r.end[0]) - 1
        y_start = bisect_right(y, r.start[1]) - 1
        y_end = bisect_right(y, r.end[1]) - 1
        for i in range(x_start, x_end):
            for j in range(y_start, y_end):
                matrix[i][j] += 1
    t1 = time.time()
    time_first = (t1 - t0) * 1e9

    t0 = time.time()
    result = []

    for p in points:
        pos_x = bisect_right(x, p[0]) - 1
        pos_y = bisect_right(y, p[1]) - 1
        if pos_x >= 0 and pos_y >= 0:
            count = matrix[pos_x][pos_y]

            result.append(count)
    t1 = time.time()
    time_second = (t1 - t0) * 1e9

    return time_first, time_second
