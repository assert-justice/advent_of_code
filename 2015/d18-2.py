def parse_lines(lines, g):
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                g.add( (x,y,) )

def pretty_grid(g, width):
    grid = [['.' for _ in range(width)] for _ in range(width)]
    for light in g:
        x, y = light
        grid[y][x] = '#'
    for row in grid:
        print(''.join(row))

def get_adj(g, width, light):
    x, y = light
    adj = []
    for i in range(-1, 2):
        for f in range(-1, 2):
            nx = x + i
            ny = y + f
            if nx < 0 or ny < 0:
                continue
            if nx == width or ny == width:
                continue
            if i == 0 and f == 0:
                continue
            # if (nx, ny) in g:
            #     adj += 1
            adj.append( (nx, ny,) )
    return adj

def sim(g, width):
    ng = set()
    g.add( (0,0) )
    g.add( (width - 1,0) )
    g.add( (0,width - 1) )
    g.add( (width - 1,width - 1) )
    for light in g:
        adj = get_adj(g, width, light)
        empty = [l for l in adj if not l in g]
        lit = len(adj) - len(empty)
        if lit == 2 or lit == 3:
            ng.add(light)
        for l in empty:
            if len(['' for lit in get_adj(g, width, l) if lit in g]) == 3:
                ng.add(l)
    return ng

f = open('2015/d18i.txt')
text = f.read()
lines = text.splitlines()
width = len(lines)
g = set()
parse_lines(lines, g)
# pretty_grid(g, width)
# g = sim(g, width)
# print('')
# pretty_grid(g, width)
for _ in range(100):
    g = sim(g, width)
g.add( (0,0) )
g.add( (width - 1,0) )
g.add( (0,width - 1) )
g.add( (width - 1,width - 1) )
print(len(g))