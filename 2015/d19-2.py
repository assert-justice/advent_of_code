def parse_lines(lines):
    rep = {}
    for line in lines:
        if line == '':
            break
        val, key = line.split(' => ')
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
        i = f + len(pattern)
        if 'e' in out and len(out) > 1:
            continue
        outputs.add(out)

def apply(rep, outputs, start):
    for rule in rep:
        for out in rep[rule]:
            str_replace(outputs, start, rule, out)
    return outputs

def solve(rep, goal):
    mols = {goal}
    steps = 0
    while not 'e' in mols:
        steps += 1
        nmols = set()
        for mol in mols:
            apply(rep, nmols, mol)
        mols = nmols
        #print(mols)
        print(steps, 'steps, ', len(mols), ' molecules found')
    #print(steps)    

f = open('2015/d19i.txt')
text = f.read()
lines = text.splitlines()

rep, start = parse_lines(lines)
solve(rep, start)