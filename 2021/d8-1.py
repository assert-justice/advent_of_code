from rich import print

lookup = {
    0:"abcefg",
    1:"cf",
    2:"acdeg",
    3:"acdfg",
    4:"bcdf",
    5:"abdfg",
    6:"abdefg",
    7:"acf",
    8:"abcdefg",
    9:"abcdfg",
}

def count(line):
    line = line.split("|")[1]
    line = line.split(" ")[1:]
    unique = [2, 4, 3, 7]
    #print(line)
    print([c for c in line if len(c) in unique])
    return len([c for c in line if len(c) in unique])

f = open('2021/d8i.txt')
text = f.read()
f.close()
lines = text.splitlines()
# for line in lines:
#     count(line)
s = sum(count(line) for line in lines)
print(s)