import math
def parse_lines(lines):
    rep = []
    for line in lines:
        if line == '':
            break
        val, key = line.split(' => ')
        rep.append((key, val,))
    rep = sorted(rep, key=lambda r: -len(r[0]))
    return rep, lines[-1]

# def str_replace(outputs, start, pattern, replace):
#     i = 0
#     while True:
#         f = start.find(pattern, i)
#         if f == -1:
#             return
#         front = start[:f]
#         back = start[f + len(pattern):]
#         out = front + replace + back
#         i = f + len(pattern)
#         if 'e' in out and len(out) > 1:
#             continue
#         outputs.add(out)

# def solve(rep, goal):
#     mols = {goal}
#     steps = 0
#     while not 'e' in mols:
#         steps += 1
#         nmols = set()
#         for mol in mols:
#             for rule in rep:
#                 str_replace(nmols, mol, rule[0], rule[1])
#         mols = nmols
#         print(steps, 'steps, ', len(mols), ' molecules found')
least_steps = math.inf
def str_replace(reps, start, pattern, replace, osteps):
    global least_steps
    if osteps == least_steps:
        return
    i = 0
    while True:
        f = start.find(pattern, i)
        if f == -1:
            break
        front = start[:f]
        back = start[f + len(pattern):]
        out = front + replace + back
        if out == 'e':
            print(osteps)
            least_steps = osteps
        i = f + len(pattern)
        if 'e' in out:
            continue
        solve(reps, out, osteps)

def solve(reps, start, osteps):
    for rep in reps:
        str_replace(reps, start, rep[0], rep[1], osteps + 1)


f = open('2015/d19i.txt')
text = f.read()
lines = text.splitlines()

rep, start = parse_lines(lines)
solve(rep, start, 0)
print('least steps:', least_steps)