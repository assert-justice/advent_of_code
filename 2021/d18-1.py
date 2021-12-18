import math, copy

def explode(ls):
    ls = copy.deepcopy(ls)
    exploded = False
    xs = []
    add_queue = []
    def spam(ls, d):
        nonlocal exploded
        if isinstance(ls, dict):
            if len(add_queue) > 0:
                ls["val"] += add_queue.pop()
            xs.append(ls)
            return ls
        else:
            if d == 4 and not exploded:
                exploded = True
                vl = ls[0]["val"]
                vr = ls[1]["val"]
                if len(xs) > 0:
                    xs[-1]["val"] += vl
                add_queue.append(vr)
                return {"val":0}
            else:
                return [spam(ls[0], d+1), spam(ls[1], d+1)]
    s = spam(ls, 0)
    if exploded:
        return s

def split(ls):
    ls = copy.deepcopy(ls)
    did_it = False
    def spam(ls):
        nonlocal did_it
        if isinstance(ls, dict):
            if ls["val"] > 9 and not did_it:
                did_it = True
                l = math.floor(ls["val"] / 2)
                h = math.ceil(ls["val"] / 2)
                return [{"val": l},{"val": h}]
            else:
                return ls
        else:
            return [spam(ls[0]), spam(ls[1])]
    s = spam(ls)
    if did_it:
        return s

def mag(ls):
    if isinstance(ls, dict):
        return ls["val"]
    else:
        vl = mag(ls[0])
        vr = mag(ls[1])
        return vl * 3 + vr * 2

def parse(line):
    p = eval(line)

    def dictate(ls, d):
        if isinstance(ls, int):
            return {"val": ls}
        else:
            return [dictate(ls[0], d+1), dictate(ls[1], d+1)]
    return dictate(p, 0)

def redux(ls):
    while True:
        e = explode(ls)
        if e:
            #print("explode!")
            ls = e
            continue
        s = split(ls)
        if s:
            #print("split!")
            ls = s
            continue
        break
    return ls

def solve(lines):
    lines = [parse(line) for line in lines]
    acc = lines.pop(0)
    for line in lines:
        acc = redux([acc, line])
    print(mag(acc))

f = open('2021/d18i.txt')
text = f.read()
f.close()

lines = text.splitlines()
solve(lines)
# a = parse('[[[[4,3],4],4],[7,[[8,4],9]]]')
# b = parse('[1,1]')
# c = parse('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')
# print(mag(c))
# print(split(c))
# r = redux([a,b])
# print(r)