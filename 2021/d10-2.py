from os import truncate
from rich import print
# time : 30 mins
# rank : 3660

total = []

def parse(line):
    global total
    lookup = {
        "(":")",
        "[":"]",
        "{":"}",
        "<":">"
    }
    points = {
        ")":1,
        "]":2,
        "}":3,
        ">":4
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
                #total += points[c]
                return False
    #print(stk)
    count = 0
    for c in reversed(stk):
        count *= 5
        count += points[lookup[c]]
    total.append(count)
    return True

f = open('2021/d10i.txt')
text = f.read()
lines = text.splitlines()
f.close()

for line in lines:
    if not parse(line):
        pass
total.sort()
print(total[len(total) // 2])