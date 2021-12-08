from rich import print
import copy
from itertools import permutations
# time: 1:43
# ranking: 5013

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

def attempt(strings, perm):
    lu = {}
    for idx, c in enumerate("abcdefg"):
        lu[c] = perm[idx]
    # for each entry in lookup
    # find all strings with the correct length
    # for each character in the lookup string
    # eliminate any string that lacks that character
    # if the number of matching strings is not exactly 1 return false
    rev = {}
    for num, lookup_str in lookup.items():
        cands = [s for s in strings if len(s) == len(lookup_str)]
        #print(list(cands))
        for c in lookup_str:
            newc = lu[c]
            cands = list(filter(lambda s: newc in s, cands))
            #print(c, newc, cands)
            if len(cands) == 0:
                return False
        cands = list(cands)
        if len(cands) != 1:
            return False
        rev[cands[0]] = num
    return rev

def crunch(line):
    start, end = line.split("|")
    start = start.split(" ")[:-1]
    end = end.split(" ")[1:]
    start = ["".join(sorted([c for c in s])) for s in start]
    end = ["".join(sorted([c for c in s])) for s in end]
    perm = permutations([c for c in "abcdefg"])
    a = None
    for p in perm:
        p = "".join(p)
        a = attempt(start, p)
        if a:
            break
    o = [a[s] for s in end]
    return int("".join([str(n) for n in o]))
    #attempt(start, "deafgbc")
    # unique = [1,4,7,8]
    # poss = {}
    # llook = {}
    # lett = "abcdefg"
    # for c in lett:
    #     poss[c] = set([c for c in lett])
    # for num in unique:
    #     expected = lookup[num]
    #     actual = [s for s in start if len(s) == len(expected)][0]
    #     llook[num] = actual
    #     for c in actual:
    #         poss[c] = set([c for c in poss[c] if c in expected])
    
    # print(llook)
    # print(poss)


f = open('2021/d8i.txt')
text = f.read()
f.close()
lines = text.splitlines()
#c = crunch("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf")
t = 0
for idx, line in enumerate(lines):
    c = crunch(line)
    t += c
    print(f"line {idx}: {c}")
print(t)