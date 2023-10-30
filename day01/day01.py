f = open(file="input.txt", mode="r")

elf, elfs = 0, []

for line in f:
    try:
        elf += int(line)
    except:
        elfs.append(elf)   
        elf = 0 

elfs.append(elf)  
a = max(elfs)

print("1a:", a)

elfs.sort(reverse=True)
b = elfs[0] + elfs[1] + elfs[2]

print("1b:", b)
