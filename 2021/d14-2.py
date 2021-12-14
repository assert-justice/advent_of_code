from rich import print
# time: 3 hours 8 minutes
# rank: 8098

def parse(lines):
    src = lines[0]
    rules = {}
    lines = lines[2:]
    for line in lines:
        s, e = line.split(" -> ")
        rules[s] = e
    return rules, src

def net_gen(rules):
    rs = {}
    for s, b in rules.items():
        cs = []
        a,c = s
        if a+b in rules:
            cs.append(a+b)
        if b+c in rules:
            cs.append(b+c)
        rs[s] = cs
    return rs

def super_freq(rules, net):
    lookup = {}
    for s,e in rules.items():
        f = freq(e)
        lookup[s] = [f]
    for i in range(1,40):
        for rule, options in net.items():
            row = lookup[rule]
            nf = {}
            for option in options:
                fs = lookup[option]
                idx = i-1
                f = fs[idx]
                nf = freq_add(nf, f)
            row.append(nf)
    return lookup

def freq_eql(f1, f2):
    if len(f1) != len(f2):
        return False
    for k,v in f1.items():
        if not k in f2:
            return False
        if f2[k] != v:
            return False
    return True

def freq_add(f1, f2):
    fs = {}
    for k,v in f1.items():
        if not k in fs:
            fs[k] = 0
        fs[k]+=v
    for k,v in f2.items():
        if not k in fs:
            fs[k] = 0
        fs[k]+=v
    return fs

def freq(src, f = None):
    if not f:
        f = {}
    for c in src:
        if not c in f:
            f[c] = 0
        f[c] += 1
    return f

def solve(src, lookup):
    f = {}
    for idx,c in enumerate(src[:-1]):
        c1 = src[idx + 1]
        k = c + c1
        for l in lookup[k]:
            f = freq_add(f, l)
        #f = freq_add(f, lookup[k][-1])
    f = freq(src, f)
    return f

def apply(rules, src):
    out = []
    for idx, c in enumerate(src[:-1]):
        out.append(c)
        c2 = src[idx + 1]
        s = c + c2
        if s in rules:
            out.append(rules[s])
    out.append(src[-1])
    return "".join(out)

f = open('2021/d14i.txt')
text = f.read()
f.close()

lines = text.splitlines()
rules, src = parse(lines)
net = net_gen(rules)
lookup = super_freq(rules, net)
# solve_f = solve("OO", lookup)
# out = "OO"
# for _ in range(10):
#     out = apply(rules, out)
# print(solve_f)
# print(freq(out))
# print("sim", fs["OO"][i-1])
f = solve(src, lookup)
s = sorted(f.items(), key= lambda x: x[1])
print(s)
print(s[-1][1] - s[0][1])