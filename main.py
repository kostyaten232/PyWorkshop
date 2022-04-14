from random import random as rr
from linear import linear
from binary import binary

n = 10_000
array = [n for n in range(n + 1)]


def rotate(array):
    for _ in range(rr(1, len(array))):
        array.append(array.pop(0))
        return array


array = rotate(array)

print(linear(array))
print(binary(array, 0, len(array) - 1))

from wrapper import get_time


@get_time
def linear(arr):
    i = 1
    for num in arr:
        i += 1
        if num > arr[arr.index(num) + 1]:
            return num, i
    return None
