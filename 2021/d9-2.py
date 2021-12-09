from rich import print
# time: 43 minutes
# rank: 3404

def get_grid(lines):
    g = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            key = (x,y,)
            val = int(c)
            g[key] = val
    return g

def is_lowest(grid, key):
    val = grid[key]
    ox,oy = key
    ds = [
        (1,0,),
        (0,1,),
        (-1,0,),
        (0,-1,)
    ]
    for d in ds:
        k = (ox + d[0],oy + d[1],)
        if k in grid and grid[k] <= val:
            return False
    return True

def get_ns(grid, key, vis):
    ox,oy = key
    ds = [
        (1,0,),
        (0,1,),
        (-1,0,),
        (0,-1,)
    ]
    ns = []
    for d in ds:
        k = (ox + d[0],oy + d[1],)
        if k in grid and grid[k] != 9 and not k in vis:
            ns.append(k)
    return ns

def ff(grid, key):
    open = set([key])
    closed = set()
    while len(open) > 0:
        temp = set()
        for k in open:
            closed.add(k)
            ns = get_ns(grid, k, closed)
            for n in ns:
                temp.add(n)
        open = temp
    #print(closed)
    return len(closed)
f = open('2021/d9i.txt')
text = f.read()
f.close()
lines = text.splitlines()
g = get_grid(lines)
ls = [k for k, n in g.items() if is_lowest(g, k)]
ls = list(ff(g, l) for l in ls)
ls.sort()
print(ls[-1] * ls[-2] * ls[-3])
#print(ls[2])
#print(ff(g, ls[2]))