def count(goal, amount, jugs, group):
    #print(amount, jugs)
    if amount == goal:
        return (len(group),)
    elif amount > goal:
        return tuple()
    elif len(jugs) == 0:
        return tuple()
    jugs = set(jugs)
    jug = jugs.pop()
    return count(goal, amount + jug[0], jugs, group + jug) + count(goal, amount, jugs, group)

f = open('2015/d17i.txt')
text = f.read()
lines = text.splitlines()
jugs = {(int(line), i,) for i, line in enumerate(lines)}
s = [n for n in count(150, 0, jugs, tuple())]
m = min(s)
l = len([n for n in s if n == m])
print(s, m, l)