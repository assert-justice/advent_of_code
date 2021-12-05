def parse_line(line):
    line = line[1:]
    id, line = line.split("@")
    pos, dim = line.split(":")
    ox, oy = pos.split(",")
    w, h = dim.split("x")
    return id.strip(), int(ox), int(oy), int(w), int(h)

def claim(cloth, rect):
    id, ox, oy, w, h = rect
    #print(id)
    contested = False
    for i in range(w):
        for f in range(h):
            key = (ox + i, oy + f,)
            if not key in cloth:
                cloth[key] = 0
            #print(key)
            #print(cloth[key])
            if cloth[key] != 1:
                contested = True
            cloth[key] += 1
    #print()
    return contested

def solve(lines):
    cloth = {}
    rects = map(parse_line, lines)
    for rect in rects:
        claim(cloth, rect)
    rects = map(parse_line, lines)
    for rect in rects:
        if not claim(cloth, rect):
            print(rect[0])
            return

f = open('2018/d3i.txt')
text = f.read()
lines = text.splitlines()
solve(lines)