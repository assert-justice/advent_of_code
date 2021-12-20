from itertools import  permutations
'''
rots where facing x = +x
y = +y, z = +z
y = +z, z = -y
y = -y, z = -z
y = -z, z = +y

rots where facing x = -x
y = -y, z = +z
y = -z, z = -y
y = +y, z = -z
y = +z, z = +y

if x = +x
y & z "want" to be the same
if x = -x
y & z "want" to be differentw 

find all combos with duplicates by
finding all permutes of x,y,z
find all permutations of + and -

3! * 2^3
6 * 8 = 
'''
def all_rot(points):
    # pick x axis (x, -x, y, -y, z, -z)
    # rotate y and z through remaining possibilities
    axes = list(permutations([0,1,2]))
    flips = [bin(n)[2:] for n in range(8)]
    flips = [(3 - len(n)) * '0' + n for n in flips]
    flips = [[1 if f == '0' else -1 for f in n] for n in flips]
    print(axes)
    print(flips)
    #return
    out = []
    for a in axes:
        for f in flips:
            nps = []
            if check_rot(a, f):
                continue
            for p in points:
                k = rot(a,f,p)
                nps.append(k)
                # x = p[a[0]] * f[0]
                # y = p[a[1]] * f[1]
                # z = p[a[2]] * f[2]
                # nps.append((x,y,z,))
            out.append(nps)
    return out

def check_rot(axis, flip):
    unit = (1,2,3)
    correct = [(1, 2, 3), (1, -3, 2), (1, -2, -3), (1, 3, -2), (-1, -2, 3), (-1, -3, -2), (-1, 2, -3), (-1, 3, 2), (2, 3, 1), (2, -1, 3), (2, -3, -1), (2, 1, -3), (-2, -3, 1), (-2, -1, -3), (-2, 3, -1), (-2, 1, 3), (3, 1, 2), (3, -2, 1), (3, -1, -2), (3, 2, -1), (-3, -1, 2), (-3, -2, -1), (-3, 1, -2), (-3, 2, 1)]
    r = rot(axis, flip, unit)
    if r in correct:
        print(correct.index(r))
        return True
    return False
    a = (r[0], 0, 0)
    b = (0, r[1], 0)
    #c = (0, 0, r[1])
    c0x = a[1]*b[2] - a[2]*b[1]
    c0y = a[2]*b[0] - a[0]*b[2]
    c0z = a[0]*b[1] - a[1]*b[0]
    return c0x == 0 and c0y == 0 and c0z == r[1]

def rot(a, f, p):
    x = p[a[0]] * f[0]
    y = p[a[1]] * f[1]
    z = p[a[2]] * f[2]
    return (x,y,z,)

def match(ps1, ps2):
    ds = {}
    for p1 in ps1:
        for p2 in ps2:
            dis = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2
            if not dis in ds:
                ds[dis] = 0
            ds[dis] += 1
    for v in ds.values():
        if v > 11:
            return True
    return False

def parse(lines):
    scanners = []
    for line in lines:
        if "scanner" in line:
            num = int(line.split(" ")[2])
            scanners.append([])
        elif len(line) == 0:
            pass
        else:
            a,b,c = line.split(",")
            a,b,c = int(a),int(b),int(c)
            scanners[-1].append((a,b,c,))
    return scanners

def get_count(res):
    out = set()
    for _, r in res:
        for p in r:
            out.add(p)
    return out

def solve(lines):
    scanners = parse(lines)
    srs = [all_rot(s) for s in scanners]
    scans = ((0, scanners[0],),)
    #print(scans)
    def rep(scans):
        if len(scans) == len(srs):
            return scans
        #print("here")
        #print(scans)
        fixed = list(map(lambda s: s[0], scans))
        print(fixed)
        for idx, rs in enumerate(srs):
            if idx in fixed:
                continue
            for r1 in map(lambda s: s[1], scans):
                for r2 in rs:
                    if match(r1, r2):
                        temp = scans + ((idx, r2,),)
                        temp = rep(temp)
                        if temp:
                            return temp
        return False
    res = rep(scans)
    #print(res)
    #print(len(res))
    #return
    unq = get_count(res)
    print(len(unq))
    return
    ex = set()
    with open("2021/temp.txt") as f:
        ls = f.read().splitlines()
        for l in ls:
            x,y,z = l.split(",")
            x,y,z = int(x),int(y),int(z)
            k = (x,y,z,)
            ex.add(k)
        e = ex.difference(unq)
        print(len(unq))
        print(len(ex))
        print(len(unq) - len(ex))
        print(len(e))
        print(len(unq.difference(ex)))

    #print(len(res))
    # for i in range(100):
    #     if len(scans) == len(scanners):
    #         break
    #     print(i)
    #     for idx, rs in enumerate(srs):
    #         for r in rs:
    #             if match(scanners[0], r):
    #                 print(f"match {idx}!")

# r = all_rot([(1,2,3,)])
# r = list(map(lambda x: x[0], r))
# print(r)
# print(len(r))
f = open('2021/d19i.txt')
text = f.read()
f.close()

lines = text.splitlines()
solve(lines)
# res = []
# for line in lines:
#     x,y,z = line.split(" ")
#     x,y,z = int(x),int(y),int(z)
#     res.append((x,y,z,))
# print(res)
# solve(lines)
# (1, 2, 3), 
# (1, 2, -3), 
# (1, -2, 3), 
# (1, -2, -3), 
# (1, 3, 2), 
# (1, 3, -2), 
# (1, -3, 2), 
# (1, -3, -2), 
# (2, 1, 3), 
# (2, 1, -3), 
# (2, -1, 3), 
# (2, -1, -3), 
# (2, 3, 1), 
# (2, 3, -1), 
# (2, -3, 1), 
# (2, -3, -1), 
# (3, 1, 2), 
# (3, 1, -2), 
# (3, -1, 2), 
# (3, -1, -2), 
# (3, 2, 1), 
# (3, 2, -1), 
# (3, -2, 1), 
# (3, -2, -1)
