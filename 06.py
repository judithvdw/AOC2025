from math import prod


def calc(s):
    ns = s[:-1]
    operator = s[-1]
    if operator == '+':
        return sum(ns)
    else:
        return prod(ns)


with open('inputs/test.txt') as f:
    rows = f.read().splitlines()

num_rows = [list(map(int, row.split())) for row in rows[:-1]]
operators = rows[-1].split()
sums = list(zip(*(num_rows + [operators])))
print(sums)

print(sum(calc(s) for s in sums))
#
# cuts = set()
# for i, char in enumerate(rows[-1][1:]):  # loop over the operators, except the first to find the cuts
#     if char != ' ':
#         cuts.add(i)
#
# split_rows = []
# for row in rows[:-1]: # don't need to do this for the operators
#     cur_row = []
#     buffer = ''
#     for i, char in enumerate(row):
#         if i in cuts:
#             cur_row.append(buffer)
#             buffer = ''
#         else:
#             buffer += char
#     cur_row.append(buffer)
#     split_rows.append(cur_row)
#
# to_calc = list(zip(*split_rows))
# pivoted = [list(map(lambda t: int("".join(t)), zip(*n))) for n in to_calc]
#
# print(pivoted)
#
#
#
