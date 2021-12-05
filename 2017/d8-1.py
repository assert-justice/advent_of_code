def parse_line(line):
    line = line.split(' ')
    reg, op, val, _, r0, cond, v0 = line
    val = int(val)
    v0 = int(v0)
    return reg, op, val, r0, cond, v0

def interp(lines):
    regs = {}
    greatest = 0
    def read(reg):
        if not reg in regs:
            regs[reg] = 0
        return regs[reg]
    def write(reg, val):
        nonlocal greatest
        if val > greatest:
            greatest = val
        regs[reg] = val
    def inc(reg, val):
        write(reg, read(reg) + val)
    def dec(reg, val):
        write(reg, read(reg) - val)
    def condition(reg, op, val):
        comp = read(reg)
        if op == '==':
            return comp == val
        elif op == '<':
            return comp < val
        elif op == '>':
            return comp > val
        elif op == '<=':
            return comp <= val
        elif op == '>=':
            return comp >= val
        elif op == '!=':
            return comp != val
    instrs = [parse_line(line) for line in lines]
    for instr in instrs:
        reg, op, val, r0, cond, v0 = instr
        if condition(r0, cond, v0):
            if op == 'inc':
                inc(reg, val)
            else:
                dec(reg, val)
    #print(regs)
    print(max(regs.values()))
    print(greatest)

f = open('2017/d8i.txt')
text = f.read()
f.close()
lines = text.splitlines()
interp(lines)