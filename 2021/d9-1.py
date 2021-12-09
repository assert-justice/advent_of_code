from rich import print

def grid(lines):
    w = len(lines[0])
    h = len(lines)
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
f = open('2021/d9i.txt')
text = f.read()
f.close()
lines = text.splitlines()
g = grid(lines)
s = sum(n + 1 for k, n in g.items() if is_lowest(g, k))
print(s)