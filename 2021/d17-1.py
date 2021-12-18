def parse(src):
    src = src.split(":")[1]
    xr, yr = src.split(",")
    xr = list(map(int, xr[3:].split("..")))
    yr = list(map(int, yr[3:].split("..")))
    return xr, yr

def step(x, y, dx, dy):
    x += dx
    y += dy
    if dx > 0:
        dx -= 1
    else:
        dx += 1
    dy -= 1
    return x, y, dx, dy

def sim(dx, dy, xr, yr):
    x = 0
    y = 0
    my = 0
    while True:
        x, y, dx, dy = step(x, y, dx, dy)
        if y > my:
            my = y
        #print("x:", x, "y:", y)
        if y < yr[0]:
            return 0
        if y <= yr[1] and x >= xr[0] and x <= xr[1]:
            return my

def guess(xr, yr):
    best = 0
    hits = 0
    for dy in range(200):
        for dx in range(100):
            h = sim(dx, dy, xr, yr)
            if h == 5671:
                print(dy)
                return
            if h:
                hits += 1
            if h > best:
                best = h
    print(best)
xr, yr = parse("target area: x=230..283, y=-107..-57")
#xr, yr = parse("target area: x=20..30, y=-10..-5")
guess(xr, yr)
#print(sim(6, 9, xr, yr))
