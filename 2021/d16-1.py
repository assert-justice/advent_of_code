def to_bin(text):
    out = []
    for c in text:
        n = int(c, 16)
        b = bin(n)[2:]
        b = (4 - len(b)) * "0" + b
        out.append(b)
    return "".join(out)

def parse(src):
    cur = 0
    vs = 0
    def group():
        nonlocal cur
        #t = 0
        # while eat(1) == 1:
        #     t += eat(4)
        # t += eat(4)
        # return t
        bs = []
        while True:
            s = src[cur:cur+5]
            bs.append(s[1:])
            cur += 5
            if s[0] == "0":
                break
        return int("".join(bs), 2)
    def eat(count):
        nonlocal cur
        n = int(src[cur:cur+count], 2)
        cur+=count
        return n
    def p_parse(d):
        nonlocal cur, vs
        v = eat(3)
        vs += v
        h = eat(3)
        lookup = {0: "sum", 1: "pro", 2: "min", 3:"max", 4:"lit", 5:"gth", 6:"lth", 7:"eql"}
        #print(d * " ", "h:", lookup[h])
        vals = []
        if h == 4:
            val = group()
            #print(d * " ", "val:", val)
            return val
        l = eat(1)
        if l == 0:
            n = eat(15)
            s = cur
            while cur < n + s:
                vals.append(p_parse(d+1))
        else:
            n = eat(11)
            for _ in range(n):
                vals.append(p_parse(d+1))
        if h == 0:
            #print(d * " ", "sumval:", vals)
            return sum(vals)
        if h == 1:
            out = 1
            for val in vals:
                out *= val
            return out
        if h == 2:
            #print(d * " ", "minval:", min(vals))
            return min(vals)
        if h == 3:
            return max(vals)
        if h == 5:
            return int(vals[0] > vals[1])
        if h == 6:
            return int(vals[0] < vals[1])
        if h == 7:
            return int(vals[0] == vals[1])
    print(p_parse(0))

f = open('2021/d16i.txt')
text = f.read()
f.close()

p = to_bin(text)
parse(p)