from rich import print

def parse(lines):
    nodes = {}
    big = set()
    def add(f, s):
        if not f in nodes:
            nodes[f] = []
        nodes[f].append(s)
    for line in lines:
        f, s = line.split("-")
        add(f,s)
        add(s,f)
        if f != f.lower():
            big.add(f)
        if s != s.lower():
            big.add(s)
    return nodes, big

def paths(lines):
    net, big = parse(lines)
    ps = []
    def rec(current, vis):
        if current == "end":
            ps.append(vis)
            return
        if current in vis:
            return
        vis = vis[:]
        if not current in big:
            vis.append(current)
        conn = net[current]
        for c in conn:
            rec(c, vis)
    rec("start", [])
    print(ps)
    print(len(ps))


f = open('2021/d12i.txt')
text = f.read()
f.close()
lines = text.splitlines()
paths(lines)