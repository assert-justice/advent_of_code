def csum(lines):
    cs = 0
    for line in lines:
        line = line.split('\t')
        print(line)
        line = sorted([int(n) for n in line])
        cs += line[-1] - line[0]
    print(cs)

f = open('2017/d2i.txt')
text = f.read()
lines = text.splitlines()
csum(lines)
f.close()
