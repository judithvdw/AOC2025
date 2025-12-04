from utils.parsing import parse_grid


def check_neighbours(cord, rolls):
    x, y = cord
    dx_dy = ((0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1))
    neighbours = {(x + dx, y + dy) for dx, dy in dx_dy}
    return len(rolls.intersection(neighbours))


with open('inputs/d4.txt') as f:
    rolls = parse_grid(f.read().splitlines())['@']

print(sum(check_neighbours(roll, rolls) < 4 for roll in rolls))

removed = 0
while True:
    to_remove = set()
    for roll in rolls:
        if check_neighbours(roll, rolls) < 4:
            to_remove.add(roll)
    if len(to_remove) == 0:
        break
    removed += len(to_remove)
    rolls = rolls - to_remove

print(removed)

