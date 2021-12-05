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
    print(root)

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
#print(parse_line('fwft (72) -> ktlj, cntj, xhth'))
parse(lines)