def parse_line(line, insts):
    line:list = line.split(' ')
    out = line[-1]
    if line[0] == 'NOT':
        op = line[:2]
    elif line[1] == '->':
        op = line[0]
    else:
        op = [line[1], line[0], line[2]]
    insts[out] = op

def ex(wire, insts):
    if not wire in insts:
        return int(wire)
    inst = insts[wire]
    if type(inst) == type(0):
        return inst
    if inst[0] == 'NOT':
        val = ~ex(inst[1], insts) & 65535
    elif inst[0] == 'AND':
        val = ex(inst[1], insts) & ex(inst[2], insts)
    elif inst[0] == 'OR':
        val = ex(inst[1], insts) | ex(inst[2], insts)
    elif inst[0] == 'RSHIFT':
        val = ex(inst[1], insts) >> ex(inst[2], insts)
    elif inst[0] == 'LSHIFT':
        val = ex(inst[1], insts) << ex(inst[2], insts)
    else:
        val = ex(inst, insts)
    insts[wire] = val
    return val


f = open('d7i.txt')
text = f.read()
lines = text.splitlines()

insts = {}
for line in lines:
    parse_line(line, insts)
#ex('x', insts)
#print(insts['x'])
#parse_line('NOT 255 -> bo', insts)
#print(type(0))
# print( ex('lx', insts) )
for wire in insts:
    print(wire, ex(wire, insts))
print(insts['a'])