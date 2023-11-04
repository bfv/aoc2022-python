
def main():
    f = open("day03/input.txt", mode="r")
    rucksacks = f.read().split(sep="\n")

    a, b, i = 0, 0, 0
    for i, rucksack in enumerate(rucksacks):
        part1, part2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        a += calc_char_values(set(part1).intersection(part2))
        if (i+1) % 3 == 0:
            b += calc_char_values(set(rucksacks[i]).intersection(rucksacks[i-1]).intersection(rucksacks[i-2]))

    print(f"a: {a}\nb: {b}")

def calc_char_values(s: str) -> int:
    v = 0
    for c in s:
        v += get_value(c)
    return v

def get_value(c) -> int:
    o = ord(c) - ord("a") + 1
    if o < 1:
        o = ord(c) - ord("A") + 27
    return o

main()
