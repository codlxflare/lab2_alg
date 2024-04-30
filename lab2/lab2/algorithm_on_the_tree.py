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

class Node:
    def __init__(self):
        self.modifier = 0
        self.from_ = 0
        self.to = 0
        self.left = None
        self.right = None

class Event:
    def __init__(self, start, end, operation):
        self.start = start
        self.end = end
        self.operation = operation

    def __lt__(self, other):
        return self.start < other.start

def create_nodes(number_of_nodes, offset=1):
    if number_of_nodes == 1:
        leaf = Node()
        leaf.from_ = leaf.to = offset
        return leaf
    partition = (number_of_nodes + 1) // 2
    left_branch = create_nodes(partition, offset)
    right_branch = create_nodes(number_of_nodes - partition, offset + partition)
    result = Node()
    result.left = left_branch
    result.right = right_branch
    result.from_ = offset
    result.to = offset + number_of_nodes - 1
    return result

def copy_node(node):
    copy = Node()
    copy.modifier = node.modifier
    copy.from_ = node.from_
    copy.to = node.to
    copy.left = node.left
    copy.right = node.right
    return copy

def delete_tree(root):
    if root.left:
        delete_tree(root.left)
    if root.right:
        delete_tree(root.right)
    del root

def operation(trees, is_changed, parent, root, start, end, number):
    if end <= root.from_ or root.to < start:
        return
    changed = root
    if is_changed or parent is not None:
        copy = copy_node(root)
        if parent is None:
            trees.append(copy)
        else:
            if parent.left == root:
                parent.left = copy
            else:
                parent.right = copy
        changed = copy
    if (start <= changed.from_ < end) and (start <= changed.to < end):
        changed.modifier += number
    else:
        operation(trees, is_changed, changed, changed.left, start, end, number)
        operation(trees, is_changed, changed, changed.right, start, end, number)

def go_to_leaf(trees, x, y, number_of_leaves):
    if 0 < x and 0 < y <= number_of_leaves:
        root = trees[x]
        sum_of_modifier = 0
        while root.left is not None:
            sum_of_modifier += root.modifier
            if root.left.from_ <= y <= root.left.to:
                root = root.left
            else:
                root = root.right
        sum_of_modifier += root.modifier
        return sum_of_modifier
    return 0

def third(rectangles, points):
    times = (0, 0)
    #result1 = []
    # if points == (12, 12):
    # return [1, 1, 2, 3, 0]
    if not rectangles:
        for point in points:
            result = 0
            #result1.append(result)
        return times

    t0 = time.time()
    x, y = set(), set()
    for rectangle in rectangles:
        x.add(rectangle[0][0])
        x.add(rectangle[1][0])
        y.add(rectangle[0][1])
        y.add(rectangle[1][1])
    sorted_x = sorted(x)
    sorted_y = sorted(y)

    events = []
    for rectangle in rectangles:
        start_x = bisect.bisect_right(sorted_x, rectangle[0][0])
        start_y = bisect.bisect_right(sorted_y, rectangle[0][1])
        end_y = bisect.bisect_right(sorted_y, rectangle[1][1])
        events.append((start_x, Event(start_y, end_y, 1)))

        end_x = bisect.bisect_right(sorted_x, rectangle[1][0])
        events.append((end_x, Event(start_y, end_y, -1)))

    number_of_leaves = len(y) - 1
    root = create_nodes(number_of_leaves)
    trees = [root]
    for event in sorted(events):
        if event[0] != len(trees) - 1:
            operation(trees, True, None, trees[-1], event[1].start, event[1].end, event[1].operation)
        else:
            operation(trees, False, None, trees[-1], event[1].start, event[1].end, event[1].operation)
    t1 = time.time()


    t2 = time.time()
    for point in points:
        pos_x = bisect.bisect_right(sorted_x, point[0])
        pos_y = bisect.bisect_right(sorted_y, point[1])
        result = go_to_leaf(trees, pos_x, pos_y, number_of_leaves)

    t3 = time.time()
    times = ((t1 - t0 )* 1e9, (t3 - t2)* 1e9  )
    return times
