def parse(lines):
    out = {}
    for line in lines:
        src = int(line.split(' ')[0])
        idx = line.find('<->') + 3
        dests = [int(num) for num in line[idx:].split(',')]
        out[src] = dests
    return out

def group(net):
    open = [0]
    closed = set()
    while len(open) > 0:
        temp = []
        for node in open:
            closed.add(node)
            dests = net[node]
            for d in dests:
                if not d in closed:
                    temp.append(d)
        open = temp
    print(closed)
    print(len(closed))

f = open('2017/d12i.txt')
text = f.read()
f.close()
lines = text.splitlines()
net = parse(lines)
group(net)