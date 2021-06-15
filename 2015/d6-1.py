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
    #elem = (x, y,)
    def on(elem):
        g.add( elem )
    def off(elem):
        if elem in g:
            g.remove(elem)
    def toggle(elem):
        if elem in g:
            g.remove(elem)
        else:
            g.add(elem)
    f = None
    if op[0] == 'on':
        f = on
    elif op[0] == 'off':
        f = off
    else:
        f = toggle
    for x in range(op[1], op[3] + 1):
        for y in range(op[2], op[4] + 1):
            elem = (x,y,)
            f(elem)

g = set()
# op = parse_line('turn on 0,0 through 9,9')
# op1 = parse_line('turn off 1,1 through 8,8')
# ex(op, g)
# ex(op1, g)
# print(len(g))

f = open('d6i.txt')
text = f.read()
lines = text.splitlines()

ops = [parse_line(line) for line in lines]
for op in ops:
    ex(op, g)
print(len(g))