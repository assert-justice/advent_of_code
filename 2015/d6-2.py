lit = set()

def parse_line(l):
    if l[:5] == 'turn ':
        l = l[5:]
    l = l.split(' ')
    p1 = l[1].split(',')
    p2 = l[3].split(',')
    op = [l[0], int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1])]
    return op

def ex(op, g: set):
    f = 0
    if op[0] == 'on':
        f = 1
    elif op[0] == 'off':
        f = -1
    else:
        f = 2
    for x in range(op[1], op[3] + 1):
        for y in range(op[2], op[4] + 1):
            elem = (x,y,)
            val = 0
            if elem in g:
                val = g[elem]
            val += f
            if val < 0:
                val = 0
            g[elem] = val

g = {}
# op = parse_line('turn on 0,0 through 9,9')
# op1 = parse_line('toggle 1,1 through 8,8')
# ex(op, g)
# ex(op1, g)
# #print(g)
# print(sum(g.values()))

f = open('d6i.txt')
text = f.read()
lines = text.splitlines()

ops = [parse_line(line) for line in lines]
for op in ops:
    ex(op, g)
print(sum(g.values()))