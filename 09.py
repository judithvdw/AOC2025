from utils.parsing import parse_ints
from itertools import permutations


def area(a, b):
    length = abs(a[1] - b[1]) + 1
    width = abs(a[0] - b[0]) + 1
    return length * width


with open('inputs/d9.txt') as f:
    coords = parse_ints(f.readlines())

print(max((area(a,b) for a,b in permutations(coords, 2))))
