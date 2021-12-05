def parse(lines):
    nodes = {}
    tree = {}
    for line in lines:
        name, weight, children = parse_line(line)
        tree[name] = (weight, children,)
        if not name in nodes:
            nodes[name] = []
        # loop through nodes. add *parent* relationships to nodes dict
        for child in children:
            if not child in nodes:
                nodes[child] = []
            nodes[child].append(name)
    root = ''
    for node in nodes:
        if len(nodes[node]) == 0:
            root = node
            break
    # w = get_weight(tree, root)
    # print(w)
    #rkids = tree[root][1]
    #print(rkids)
    mem = {}
    get_weight(tree, root, mem)
    name = root
    lname = None
    while True:
        kids = tree[name][1]
        lname = name
        name = get_outlier(kids, mem)
        print(name)
        if not name:
            print(lname, tree[lname][0])
            break
    # for name in mem:
    #     print(name, mem[name])
    # for kid in rkids:
    #     print(kid, get_weight(tree, kid, ))

def get_outlier(names, mem):
    kids = sorted([(name, mem[name]) for name in names], key=lambda kid: kid[1])
    print(kids)
    normal = kids[1][1]
    if kids[0][1] != normal:
        return kids[0][0]
    elif kids[-1][1] != normal:
        return kids[-1][0]
    # else return None

def get_weight(tree, name, mem):
    if name in mem:
        return mem[name]
    node = tree[name]
    weight, children = node
    for child in children:
        weight += get_weight(tree, child, mem)
    mem[name] = weight
    return weight

def parse_line(line):
    spl = line.split(' ')
    name = spl[0]
    start = line.find('(') + 1
    end = line.find(')')
    weight = int(line[start:end])
    start = line.find('->')
    children = []
    if start != -1:
        children = line[start+2:].split(',')
        children = [child.strip() for child in children]
    return name, weight, children

f = open('2017/d7i.txt')
text = f.read()
f.close()
lines = text.splitlines()
parse(lines)