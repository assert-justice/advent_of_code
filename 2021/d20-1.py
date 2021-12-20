def get_grid(lines, pad):
    out = {}
    for y in range(-pad-1, len(lines[0]) + pad + 1):
        for x in range(-pad-1, len(lines) + pad + 1):
            out[(x,y,)] = '.'
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            out[(x,y,)] = c
    return out

def count(px, py, grid):
    digits = []
    for y0 in range(-1,2):
        for x0 in range(-1,2):
            x = px + x0
            y = py + y0
            k = (x,y,)
            if not k in grid or grid[k] == '.':
                digits.append('0')
            else:
                digits.append('1')
                
    s = "".join(digits)
    n = int(s, 2)
    return n

def count0(px, py, grid):
    digits = []
    for y0 in range(-1,2):
        for x0 in range(-1,2):
            x = px + x0
            y = py + y0
            k = (x,y,)
            if not k in grid or grid[k] == '#':
                digits.append('1')
            else:
                digits.append('0')
                
    s = "".join(digits)
    n = int(s, 2)
    return n

def apply(algo, grid):
    new = {}
    for p in grid:
        px, py = p
        n = count(px, py, grid)
        new[(px,py,)] = algo[n]
    return new

def apply0(algo, grid):
    new = {}
    for p in grid:
        px, py = p
        n = count0(px, py, grid)
        new[(px,py,)] = algo[n]
    return new

def vis(grid):
    x_min = min(p[0] for p in grid)
    w = max(p[0] for p in grid) - x_min
    y_min = min(p[1] for p in grid)
    h = max(p[1] for p in grid) - y_min
    print(x_min, w, y_min, h)
    for f in range(h+1):
        y = f + y_min
        line = []
        for i in range(w+1):
            x = i + x_min
            #line.append(count(x, y, grid, {}))
            k = (x,y,)
            if k in grid and grid[k] == '#':
                line.append('#')
            else:
                line.append('.')
        line = "".join(line)
        print(line)


f = open('2021/d20i.txt')
text = f.read()
f.close()

lines = text.splitlines()
algo = lines.pop(0)
lines.pop(0)
grid = get_grid(lines, 50)
for _ in range(25):
    grid = apply(algo, grid)
    grid = apply0(algo, grid)
f = list(filter(lambda c: c == '#', grid.values()))
print(len(f))
#vis(grid)
#print(len(grid))
#c = count(2, 2, grid, {})
#print(algo[c])