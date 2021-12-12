#from rich import print

def parse(lines):
    nodes = {}
    big = set()
    def add(f, s):
        if s == "start":
            return
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
    def hd(vis):
        return len(vis) != len(set(vis))
    def rec(current, vis):
        if current == "end":
            ps.append(vis)
            if len(ps) % 1000 == 0:
                len(ps)
            #print(vis)
            return
        if current in vis:
            if hd(vis):
                return
        vis = vis[:]
        if not current in big:
            vis.append(current)
        conn = net[current]
        for c in conn:
            rec(c, vis)
    rec("start", [])
    #print(ps)
    print(len(ps))


f = open('2021/d12i.txt')
text = f.read()
f.close()
lines = text.splitlines()
paths(lines)