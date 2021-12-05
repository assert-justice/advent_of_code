def interp(ops):
    ip = 0
    steps = 0
    while ip < len(ops):
        off = ops[ip]
        if off > 2:
            ops[ip] -= 1
        else:
            ops[ip]+=1
        ip += off
        steps += 1
    print(steps)

f = open('2017/d5i.txt')
text = f.read()
f.close()
lines = text.splitlines()
ops = [int(num) for num in lines]
interp(ops)