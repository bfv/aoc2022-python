
def main():
    f = open("day03/input.txt", mode="r")
    rucksacks = f.read().split(sep="\n")

    a, b = 0, 0
    for rucksack in rucksacks:
        part1, part2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        a += calc(set(part1).intersection(part2))

    print(f"a: {a}\nb: {b}")

def calc(s: str) -> int:
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
