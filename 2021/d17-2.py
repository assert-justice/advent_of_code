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
    if dx < 0:
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
        if y < yr[0] or x > xr[1]:
            return False
        if y <= yr[1] and x >= xr[0]:
            return True

def guess(xr, yr):
    # print(sim(7, 7, xr, yr))
    # return
    hits = []
    for dy in range(-107, 110):
        for dx in range(500):
            h = sim(dx, dy, xr, yr)
            if h:
                hits.append((dx, dy))
    print(hits)
    print(len(hits))
    # with open("2021/d17i.txt") as f:
    #     txt = f.read()
    #     vals = []
    #     lines = txt.splitlines()
    #     for line in lines:
    #         line = line.split(" ")
    #         line = list(filter(lambda x: len(x) > 0, line))
    #         for v in line:
    #             v = v.split(",")
    #             v = (int(v[0]), int(v[1]),)
    #             if not v in hits:
    #                 print(v)
    #                 return
xr, yr = parse("target area: x=230..283, y=-107..-57")
#xr, yr = parse("target area: x=20..30, y=-10..-5")
guess(xr, yr)
#print(sim(6, 9, xr, yr))