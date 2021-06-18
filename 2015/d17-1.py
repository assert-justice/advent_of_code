def count(goal, amount, jugs):
    #print(amount, jugs)
    if amount == goal:
        return 1
    elif amount > goal:
        return 0
    elif len(jugs) == 0:
        return 0
    jugs = set(jugs)
    jug = jugs.pop()
    return count(goal, amount + jug[0], jugs) + count(goal, amount, jugs)

f = open('2015/d17i.txt')
text = f.read()
lines = text.splitlines()
jugs = {(int(line), i,) for i, line in enumerate(lines)}
print(count(150, 0, jugs))