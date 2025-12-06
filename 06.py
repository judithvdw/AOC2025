from math import prod


def calc(s, operator):
    if operator == '+':
        return sum(s)
    else:
        return prod(s)


def parse_spaces(rows):
    cuts = set()
    for i, char in enumerate(rows[-1][1:]):  # loop over the operators, except the first to find the cuts
        if char != ' ':
            cuts.add(i)

    split_rows = []
    for row in rows[:-1]:  # don't need to do this for the operators
        cur_row = []
        buffer = ''
        for i, char in enumerate(row):
            if i in cuts:
                cur_row.append(buffer)
                buffer = ''
            else:
                buffer += char
        cur_row.append(buffer)
        split_rows.append(cur_row)
    return split_rows


with open('inputs/d6.txt') as f:  # added an extra column of 0's and a '+' to make it work
    rows = f.read().splitlines()

number_rows = [list(map(int, row.split())) for row in rows[:-1]]
operators = rows[-1].split()

sums = list(zip(*number_rows))  # pivot the rows/cols so the right groups end up together
print(sum(calc(s, op) for s, op in zip(sums, operators)))


sums = list(zip(*parse_spaces(rows)))
pivoted = [list(map(lambda x: int(''.join(x)), zip(*s))) for s in sums]
print(sum(calc(s, op) for s, op in zip(pivoted, operators)))
