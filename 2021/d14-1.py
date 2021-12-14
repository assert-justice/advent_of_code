from rich import print

def parse(lines):
    src = lines[0]
    rules = {}
    lines = lines[2:]
    for line in lines:
        s, e = line.split(" -> ")
        rules[s] = e
    return rules, src

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

def freq(src):
    f = {}
    for c in src:
        if not c in f:
            f[c] = 0
        f[c] += 1
    return f
f = open('2021/d14i.txt')
text = f.read()
f.close()

lines = text.splitlines()
rules, src = parse(lines)
for _ in range(10):
    src = apply(rules, src)
f = freq(src)
s = sorted(f.items(), key= lambda x: x[1])
print(s[-1][1] - s[0][1])