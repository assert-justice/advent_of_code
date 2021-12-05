def parse(line):
    #Step C must be finished before step A can begin.
    dep = line[5]
    step = line[36]
    return step, dep

def get_deps(lines):
    deps = {}
    for line in lines:
        step, dep = parse(line)
        if not step in deps:
            deps[step] = []
        if not dep in deps:
            deps[dep] = []
        deps[step].append(dep)
    return deps

def solve(lines):
    deps = get_deps(lines)
    steps = []
    while len(deps) > 0:
        candids = []
        for step, deplist in deps.items():
            for dep in deplist:
                if not dep in steps:
                    break
            else:
                candids.append(step)
        candids.sort()
        step = candids[0]
        deps.pop(step)
        steps.append(step)
    print(''.join(steps))

f = open('2018/d7i.txt')
text = f.read()
lines = text.splitlines()
solve(lines)