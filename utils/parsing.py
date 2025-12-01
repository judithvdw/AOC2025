import re
from collections import defaultdict


def parse_ints(lines, negative=False):
    pattern = r'-?\d+' if negative else r'\d+'
    return [tuple(map(int, re.findall(pattern, line))) for line in lines]


def parse_grid(lines, skip="", nums=False):
    d = defaultdict(set)
    for y, line in enumerate(lines):
        for x, c in enumerate(line.strip()):
            if c not in skip:
                if nums:
                    d[int(c)].add((x, y))
                else:
                    d[c].add((x, y))
    return d
