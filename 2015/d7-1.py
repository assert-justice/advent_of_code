f = open('d7i.txt')
text = f.read()
lines = text.splitlines()

def parse_line(line):
    line:list = line.split(' ')
    out = line[-1]
    if line[0] == 'NOT':
        op = line[:2]
    elif line[1] == '->':
        op = ['LIT', line[0]]
    else:
        op = [line[1], line[0], line[2]]
    

parse_line('bn RSHIFT 2 -> bo')