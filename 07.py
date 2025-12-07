from collections import defaultdict

from utils.parsing import parse_grid


def track_routes(start, splitters, h=142, w=142):
    active_beams = defaultdict(int)
    active_beams[start.pop()] = 1
    splits = 0
    for y in range(1, h):
        for x in range(w):
            if (x, y) in splitters and (x, y - 1) in active_beams:
                splits += 1
                active_beams[(x - 1, y)] += active_beams[(x, y - 1)]
                active_beams[(x + 1, y)] += active_beams[(x, y - 1)]
                del active_beams[(x, y - 1)]
            if (x, y - 1) in active_beams:
                active_beams[(x, y)] += active_beams[(x, y - 1)]
                del active_beams[(x, y - 1)]
    return splits, sum(active_beams.values())


with open('inputs/d7.txt') as f:
    grid = parse_grid(f.read().splitlines())

p1, p2 = track_routes(grid['S'], grid['^'])
print(p1)
print(p2)
