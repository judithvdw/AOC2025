from itertools import batched


def is_invalid(number):
    length = len(number)
    if length % 2 == 1:
        return False
    else:
        half = length // 2
        if number[:half] == number[half:]:
            return True
        else:
            return False


def is_invalid_2(number):
    length = len(number)
    numbers = set()
    for i in range(1, length // 2 + 1):
        if length % i == 0 and len(set(batched(number, i))) == 1:
            if number not in numbers:
                yield int(number)
                numbers.add(number)


with open('inputs/d2.txt') as f:
    codes = f.read().strip().split(',')

total = 0
total_2 = 0
for code in codes:
    start, finish = code.split('-')
    for num in range(int(start), int(finish) + 1):
        if is_invalid(str(num)):
            total += num
        total_2 += sum(is_invalid_2(str(num)))

print(total)
print(total_2)
