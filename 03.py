def joltage(bank, n):
    bank = list(map(int, list(bank)))
    jolts = []
    while len(jolts) < n:
        needed = n-len(jolts)
        if needed == 1:
            num = max(bank)
        else: # don't consider last places, because we still need more numbers after
            num = max(bank[:-needed+1])
        jolts.append(num)
        loc = bank.index(num)
        bank = bank[loc+1:]
    ret = int("".join(map(str, jolts)))
    return ret


with open('inputs/d3.txt') as f:
    banks = f.read().splitlines()
    print(sum(joltage(bank, n=2) for bank in banks))
    print(sum(joltage(bank, n=12) for bank in banks))


