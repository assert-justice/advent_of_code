def parse(lines):
    out = []
    for line in lines:
        line = line.split(':')
        out.append(
            (int(line[0]), int(line[1]),)
            )
    return out

def sev(layers, wait):
    cost = 0
    for layer, range in layers:
        range_ex = range * 2 - 2
        time = layer + wait
        pos = time % range_ex
        if pos == 0:
            cost += 1
    return cost

def find(layers):
    wait = 0
    while sev(layers, wait) > 0:
        wait += 1
        if wait%1000 == 0:
            print(wait)
    print(wait)

f = open('2017/d13i.txt')
text = f.read()
f.close()
lines = text.splitlines()
layers = parse(lines)
find(layers)
#print(sev(layers,10))