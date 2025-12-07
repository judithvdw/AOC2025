from utils.parsing import parse_grid


def run_simulation(start, splitters, h=16, w=16):
    active_beams = start
    splits = 0
    for y in range(1, h):
        for x in range(w):
            if (x, y) in splitters and (x, y - 1) in active_beams:
                splits += 1
                active_beams.update({(x - 1, y), (x + 1, y)})
                active_beams.remove((x, y - 1))
            if (x, y - 1) in active_beams:
                active_beams.add((x, y))
    return splits


with open('inputs/d7.txt') as f:
    grid = parse_grid(f.read().splitlines())
    splitters = grid['^']
    start = grid['S']

print(run_simulation(start, splitters, 142, 142))
