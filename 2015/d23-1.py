def parse(line):
    line = line.replace('+', '')
    line = line.replace(',', '')
    line = line.split(' ')
    def conv(idx):
        if idx < len(line):
            if line[idx] != 'a' and line[idx] != 'b':
                line[idx] = int(line[idx])
    conv(1)
    conv(2)
    return tuple(line)

def interp(program):
    ip = -1
    reg = {
        'a' : 1,
        'b' : 0,
    }
    while ip < len(program)-1:
        ip += 1
        inst = program[ip]
        op = inst[0]
        if op == 'hlf':
            reg[inst[1]] //= 2
        elif op == 'tpl':
            reg[inst[1]] *= 3
        elif op == 'inc':
            reg[inst[1]] += 1
        elif op == 'jmp':
            ip += inst[1] - 1
        elif op == 'jie' and reg[inst[1]] % 2 == 0:
            ip += inst[2] - 1
        elif op == 'jio' and reg[inst[1]] == 1:
            ip += inst[2] - 1
    print(reg)
        

f = open('2015/d23i.txt')
text = f.read()
lines = text.splitlines()
program = [parse(line) for line in lines]
interp(program)