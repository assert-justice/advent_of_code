from rich import print
# time: 37 mins
# rank: 2938

def parse(lines:list):
    fs = []
    ds = set()
    idx = lines.index("")
    for line in lines[:idx]:
        x, y = line.split(",")
        ds.add((int(x), int(y),))
    for line in lines[idx+1:]:
        arg = line.split(" ")[2]
        f, l = arg.split("=")
        fs.append((f,int(l),))
    return ds, fs

def fold(ds, f):
    a, l = f
    nds = set()
    if a == "y":
        for d in ds:
            y = d[1]
            if y > l:
                y = l - (y - l)
                nds.add((d[0], y,))
            else:
                nds.add(d)
    else:
        for d in ds:
            x = d[0]
            if x > l:
                x = l - (x - l)
                nds.add((x, d[1],))
            else:
                nds.add(d)
    return nds

def vis(ds):
    w = 0
    h = 0
    for x,y in list(ds):
        if x > w:
            w = x
        if y > h:
            h = y
    for y in range(h+1):
        s = "".join(["#" if (x,y,) in ds else "." for x in range(w+1)])
        print(s)
    print()


f = open('2021/d13i.txt')
text = f.read()
f.close()

lines = text.splitlines()
ds, fs = parse(lines)
for f in fs:
    ds = fold(ds, f)
    break
print(len(ds))