#from rich import print
import math

def grid_gen(lines):
    grid = {}
    h = len(lines)
    w = len(lines[0])
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x,y,)] = int(c)
    return grid, w, h

def on_grid(cell, w, h):
    if cell[0] < 0 or cell[1] < 0:
        return False
    if cell[0] >= w * 5 or cell[1] >= h * 5:
        return False
    # if cell[0] >= w or cell[1] >= h:
    #     return False
    return True


def value(grid, w, h, cell):
    if cell in grid:
        return grid[cell]
    # if abs(cell[0] - cell[1]) > 100:
    #     return math.inf
    c = 0
    c += cell[0] // w
    c += cell[1] // h
    x = cell[0] % w
    y = cell[1] % h
    c += grid[(x,y,)]
    i = 0
    l = 0
    while i < c:
        l += 1
        if l == 10:
            l = 1
        i += 1
    return l

def pathfind(lines):
    grid, w, h = grid_gen(lines)
    #print(value(grid, w, h, (10, 10,)))
    #return
    op = {(0,0,):[0, None]}
    cl = {}
    dirs = [
        (1,0,),
        (0,1,),
        (-1,0,),
        (0,-1,),
    ]
    best = None
    while True:
        best = min(op, key=lambda cell: op[cell][0])
        val = op.pop(best)
        cl[best] = val
        if best == (w*5 - 1, h*5 - 1):
            print("got here")
            break
        for d in dirs:
            k = (d[0] + best[0], d[1] + best[1],)
            if not on_grid(k, w, h) or k in cl or k in op:
                continue
            ent = [cl[best][0] + value(grid, w, h, k), best]
            if k in op and cl[k][0] < ent[0]:
                pass
            else:
                op[k] = ent
    cur = best
    t = 0
    while cur:
        ent = cl[cur]
        t += value(grid, w, h, cur)
        cur = ent[1]
    print(t - value(grid, w, h, (0,0,)))

f = open('2021/d15i.txt')
text = f.read()
f.close()

lines = text.splitlines()
pathfind(lines)