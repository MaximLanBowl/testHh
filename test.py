'''
Задание номер 1
'''


def test1(nums):
    unique_nums = []
    for num in nums:
        if nums.count(num) == 1:
            unique_nums.append(num)
    return unique_nums


"""
Задание номер 2 
"""


def test2(num) -> int:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def nums(minimum, maximum):
    simple_nums = []
    for x in range(minimum, maximum + 1):
        if test2(x):
            return simple_nums.append(x)
    return simple_nums


"""
Задание номер 3
"""

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    # с дистанцией гугл помог)

    def get_cord(self):
        return self.x, self.y

    def set_cord(self, x, y):
        self.x = x
        self.y = y


"""
Задание номер 4
"""


def length(sort):
    return len(sort)


strings = ['car', 'house', 'ship']

simple_sort = sorted(strings, key=length)

reverse_sort = sorted(strings, key=length, reverse=True)

print("Возрастание:", simple_sort)
print("Убывание:", reverse_sort)

