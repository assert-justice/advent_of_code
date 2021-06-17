def disp(jugs, goal):
    fills = set()
    def fill(amount, remaining, tup):
        if amount == goal:
            l = list(tup)
            l.sort()
            fills.add(tuple(l))
            print(l)
            return
        elif amount > goal:
            return
        for jug in remaining:
            rem = set(remaining)
            rem.remove(jug)
            fill(amount + jug[0], rem, tup + (jug,))
    fill(0, jugs, tuple())
    print(len(fills))
    # for f in fills:
    #     print(f)

f = open('d17i.txt')
text = f.read()
lines = text.splitlines()
jugs = {(int(line), i,) for i, line in enumerate(lines)}
disp(jugs, 150)