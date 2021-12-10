from os import truncate
from rich import print

total = 0

def parse(line):
    global total
    lookup = {
        "(":")",
        "[":"]",
        "{":"}",
        "<":">"
    }
    points = {
        ")":3,
        "]":57,
        "}":1197,
        ">":25137
    }
    stk = []
    for c in line:
        if c in lookup:
            stk.append(c)
        else:
            if len(stk) == 0:
                return False
            if lookup[stk[-1]] == c:
                stk.pop()
            else:
                total += points[c]
                return False
    return True

f = open('2021/d10i.txt')
text = f.read()
lines = text.splitlines()
f.close()

for line in lines:
    if not parse(line):
        print(line)
print(total)