import time
import bisect
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

def first(rectangles, points):
    start_time = time.time()
    for point in points:
        counter = 0
        for rectangle in rectangles:
            if rectangle.start[0] <= point[0] < rectangle.end[0] and rectangle.start[1] <= point[1] < rectangle.end[1]:
                counter += 1

    end_time = time.time()
    return (end_time - start_time) * 1e9

