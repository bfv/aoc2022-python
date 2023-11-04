
from dataclasses import dataclass

@dataclass
class Assignment:
    low: int
    high: int

def main():
    f = open("day04/input.txt", mode="r")
    assignment_pairs = f.read().split(sep="\n")

    a, b = 0, 0
    for p in assignment_pairs:
        pair = p.split(sep=",")
        a1, a2 = expand(pair[0]), expand(pair[1])
        if is_contained(a1, a2):
            a += 1
        if is_overlapped(a1, a2):
            b += 1
    print(f"a: {a}, b: {b}")
        
def is_contained(a1: Assignment, a2: Assignment) -> bool:
    return (a1.low <= a2.low and a1.high >= a2.high) or (a2.low <= a1.low and a2.high >= a1.high)

def is_overlapped(a1: Assignment, a2: Assignment) -> bool:
    return (
        a1.low >= a2.low and a1.low <= a2.high or
		a1.high >= a2.low and a1.high <= a2.high or
		a1.low <= a2.low and a1.high >= a2.high
    )

def expand(s: str) -> Assignment:
    p = s.split("-")
    return Assignment(low=int(p[0]), high=int(p[1]))

main()

