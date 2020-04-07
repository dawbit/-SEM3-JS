from math import tan
import math


def field():
    length = int(input())
    number = int(input())
    area = (number * length ** 2) / (4 * tan(math.pi / number))
    print(area)


field()