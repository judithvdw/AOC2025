def move_dial(current, instr):
    direction = 1 if instr[0] == "R" else -1
    n = int(instr[1:])
    new_pos = (current + direction * n) % 100

    if direction == 1:
        steps_to_zero = 100 - current
    else:
        steps_to_zero = current

    if steps_to_zero > n:
        crosses = 0
    else:
        crosses = 1 + (n - steps_to_zero) // 100

    return crosses, new_pos


with open('inputs/d1.txt') as f:
    lines = f.read().splitlines()

current = 50
zeros = 0
past_zeros = 0

for line in lines:
    crossed, current = move_dial(current, line)
    if current == 0:
        zeros += 1
    past_zeros += crossed

print(f'Part 1: {zeros}')
print(f'Part 2: {past_zeros}')
