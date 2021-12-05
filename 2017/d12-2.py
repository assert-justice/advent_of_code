def parse(lines):
    out = {}
    for line in lines:
        src = int(line.split(' ')[0])
        idx = line.find('<->') + 3
        dests = [int(num) for num in line[idx:].split(',')]
        out[src] = dests
    return out

def group(net, start):
    open = [start]
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
    return closed

def solve(net: dict):
    nodes = set(net.keys())
    groups = 0
    while len(nodes) > 0:
        start = nodes.pop()
        gr = group(net, start)
        nodes = nodes.difference(gr)
        groups += 1
    print(groups)

f = open('2017/d12i.txt')
text = f.read()
f.close()
lines = text.splitlines()
net = parse(lines)
solve(net)