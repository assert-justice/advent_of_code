from rich import print

def parse(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x,y,)] = int(c)
    return grid

def sim(grid):
    ds = [
        (0,1,),
        (1,0,),
        (0,-1,),
        (-1,0,),
        (1,1,),
        (-1,1,),
        (1,-1,),
        (-1,-1)
    ]
    # inc octopi
    for k in grid:
        grid[k] += 1
    flashed = []
    while True:
        flash = [k for k, val in grid.items() if val > 9 and not k in flashed]
        flashed += flash
        if len(flash) == 0:
            break
        for (ox, oy) in flash:
            for d in ds:
                x = ox + d[0]
                y = oy + d[1]
                k = (x,y,)
                if k in grid:
                    grid[k] += 1
    for k in grid:
        if grid[k] > 9:
            grid[k] = 0
    return grid, len(flashed)

def vis(grid):
    c = 0
    for y in range(10):
        p = []
        for x in range(10):
            v = str(grid[(x,y,)])
            if v == "0":
                c += 1
            p.append(v)
        print("".join(p))
        p = "".join([str(grid[(x,y,)]) for x in range(10)])
        print(p)
    return c

        
f = open('2021/d11i.txt')
text = f.read()
lines = text.splitlines()
f.close()

g = parse(lines)
t = 0
for i in range(100):
    g, n = sim(g)
    t += n
print(t)