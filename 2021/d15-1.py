#from rich import print

def grid_gen(lines):
    grid = {}
    h = len(lines)
    w = len(lines[0])
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            # cost, parent, weight
            # cost = parent_cost + weight
            grid[(x,y,)] = [0, None, int(c) , int(c)]
            #grid[(x,y,)] = int(c)
    return grid, w, h

def cost(grid, cell):
    ent = grid[cell]
    if ent[0] > 0:
        return ent[0]
    c = ent[2]
    if ent[1]:
        c += cost(grid, ent[1])
    return c

def pathfind(lines):
    grid, w, h = grid_gen(lines)
    op = [(0,0)]
    cl = []
    dirs = [
        (1,0,),
        (0,1,),
        (-1,0,),
        (0,-1,),
    ]
    run = True
    best = None
    while run and len(op) > 0:
    #for _ in range(10):
        best = min(op, key=lambda cell: cost(grid, cell))
        if best == (w - 1, h - 1):
            print("got here")
            run = False
        op.remove(best)
        cl.append(best)
        for d in dirs:
            k = (d[0] + best[0], d[1] + best[1],)
            if not k in grid or k in cl or k in op:
                continue
            ent = grid[k]
            if not ent[1] or cost(grid, ent[1]) > cost(grid, best):
                ent[1] = best
            op.append(k)
    # for c in cl:
    #     print(c, cost(grid,c))
    cur = best
    t = 0
    while cur:
        ent = grid[cur]
        print(cur)
        t += ent[3]
        cur = ent[1]
    print(t)

f = open('2021/d15i.txt')
text = f.read()
f.close()

lines = text.splitlines()
pathfind(lines)