def check_fresh(ingredient, ranges):
    for r in ranges:
        low, high = r
        if low < ingredient <= high:
            return True
    return False


def has_overlap(a, b):
    return a[1] >= b[0]


def merge_ranges(ranges):
    total = 0
    sorted_ranges = list(sorted(ranges))

    i = 0
    cur_min, cur_max = sorted_ranges[i]
    while i < len(sorted_ranges) - 1:
        print(cur_min, cur_max)
        i += 1
        if sorted_ranges[i][1] < cur_max:
            continue
        elif has_overlap((cur_min, cur_max), sorted_ranges[i]):
            cur_max = sorted_ranges[i][1]
        else:  # time to pop
            total += cur_max - cur_min + 1
            cur_min, cur_max = sorted_ranges[i]
    total += cur_max - cur_min + 1

    return total


with open('inputs/d5.txt') as f:
    a, b = f.read().split('\n\n')
    ranges = [tuple(map(int, r.split('-'))) for r in a.split()]
    spoiled = [int(n) for n in b.split()]

print(sum(check_fresh(ingredient, ranges) for ingredient in spoiled))
print(merge_ranges(ranges))
