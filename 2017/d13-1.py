def parse(lines):
    out = []
    for line in lines:
        line = line.split(':')
        out.append(
            (int(line[0]), int(line[1]),)
            )
    return out

def sev(layers):
    cost = 0
    for layer, range in layers:
        range_ex = range * 2 - 2
        time = layer
        pos = time % range_ex
        if pos == 0:
            cost += layer * range
    return cost

f = open('2017/d13i.txt')
text = f.read()
f.close()
lines = text.splitlines()
layers = parse(lines)
print(sev(layers))