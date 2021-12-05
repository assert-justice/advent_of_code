from rich import print
# time: 20ish minutes
# 911 people ahead of me
def parse(lines):
    out = []
    for line in lines:
        start, end = line.split("->")
        start = [int(c) for c in start.split(",")]
        end = [int(c) for c in end.split(",")]
        out.append((start, end,))
    return out

def collide(lines):
    points = {}
    sign = lambda a: (a>0) - (a<0)
    def add_point(point):
        point = tuple(point)
        if not point in points:
            points[point] = 0
        points[point] += 1
    for start, end in lines:
        dir = (sign(end[0] - start[0]), sign(end[1] - start[1]),)
        while True:
            add_point(start)
            if start == end:
                break
            start[0] += dir[0]
            start[1] += dir[1]
    print(len([v for v in points.values() if v > 1]))

f = open('2021/d5i.txt')
text = f.read()
lines = text.splitlines()
f.close()
lines = parse(lines)
collide(lines)