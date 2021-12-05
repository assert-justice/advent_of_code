def parse_line(line):
    line = line[1:]
    id, line = line.split("@")
    pos, dim = line.split(":")
    ox, oy = pos.split(",")
    w, h = dim.split("x")
    return id.strip(), int(ox), int(oy), int(w), int(h)

def claim(cloth, rect):
    _, ox, oy, w, h = rect
    for i in range(w):
        for f in range(h):
            key = (ox + i, oy + f,)
            if not key in cloth:
                cloth[key] = 0
            cloth[key] += 1

def solve(lines):
    cloth = {}
    rects = map(parse_line, lines)
    for rect in rects:
        claim(cloth, rect)
    area = 0
    for square in cloth.values():
        if square > 1:
            area += 1
    print(area)

f = open('2018/d3i.txt')
text = f.read()
lines = text.splitlines()
solve(lines)