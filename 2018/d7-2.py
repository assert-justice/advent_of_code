from rich import print, pretty
#pretty.install()

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
    workers = [["idle", 0,] for _ in range(5)]
    live = True
    ticks = 0
    while live:
        ticks += 1
        live = False
        for idx, w in enumerate(workers):
            state, time = w
            if state == 'idle':
                candids = []
                for step, deplist in deps.items():
                    for dep in deplist:
                        if not dep in steps:
                            break
                    else:
                        candids.append(step)
                if len(candids) == 0:
                    continue
                candids.sort()
                step = candids[0]
                deps.pop(step)
                w[0] = step
                w[1] = ord(step) - ord('A') + 62
                print(f"worker {idx} began task {step}", )
                live = True
            if time > 0:
                live = True
                time -= 1
                if time == 0:
                    print(f"worker {idx} finished task {state}")
                    steps.append(state)
                    state = 'idle'
                w[0] = state
                w[1] = time
    print(ticks)
    # while len(deps) > 0:
    #     candids = []
    #     for step, deplist in deps.items():
    #         for dep in deplist:
    #             if not dep in steps:
    #                 break
    #         else:
    #             candids.append(step)
    #     candids.sort()
    #     step = candids[0]
    #     deps.pop(step)
    #     steps.append(step)
    print(''.join(steps))

f = open('2018/d7i.txt')
text = f.read()
lines = text.splitlines()
solve(lines)