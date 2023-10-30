
a, b = 0, 0

p1 = { "A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6 }
p2 = { "A X": "Z", "A Y": "X", "A Z": "Y", "B X": "X", "B Y": "Y", "B Z": "Z", "C X": "Y", "C Y": "Z", "C Z": "X" }

f = open(file="input.txt", mode="r")
lines = f.read().split(sep="\n")

for line in lines:
    a += int(p1[line])
    s = line[0:1] + " " + p2[line]
    b += p1[s]

print("1a:", a)
print("1b:", b)
