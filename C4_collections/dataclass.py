

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# point = Point(3, 4)
# print(f"x = {point.x} and y = {point.y}")
# point.x = 7
# print(f"x = {point.x} and y = {point.y}")

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


point = Point(5, 6)
print(point)
print(f"x = {point.x} and y = {point.y}")
point.x = 8
print(f"x = {point.x} and y = {point.y}")
