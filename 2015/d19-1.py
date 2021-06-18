def parse_lines(lines):
    rep = {}
    for line in lines:
        if line == '':
            break
        key, val = line.split(' => ')
        if not key in rep:
            rep[key] = []
        rep[key].append(val)
    return rep, lines[-1]

def str_replace(outputs, start, pattern, replace):
    i = 0
    while True:
        f = start.find(pattern, i)
        if f == -1:
            return
        front = start[:f]
        back = start[f + len(pattern):]
        out = front + replace + back
        outputs.add(out)
        i = f + len(pattern)

def solve(rep, start):
    outputs = set()
    for rule in rep:
        for out in rep[rule]:
            str_replace(outputs, start, rule, out)
    print(len(outputs))

f = open('2015/d19i.txt')
text = f.read()
lines = text.splitlines()

rep, start = parse_lines(lines)
solve(rep, start)