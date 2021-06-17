def parse_line(line, m, p):
    line = line.split(' ')
    m[line[0] + line[2]] = int(line[4])
    m[line[2] + line[0]] = int(line[4])
    p.add(line[0])
    p.add(line[2])

def travel(m, last, remaining, length, lis):
    if len(remaining) == 0:
        lis.append(length)
    else:
        for location in remaining:
            rem = set(remaining)
            rem.remove(location)
            dis = 0
            if last != '':
                dis += m[last + location]
            travel(m, location, rem, length + dis, lis)
            
        # visit = remaining.pop()
        # travel(m, visit, remaining, m[last + visit] + length, lis)




def disp(m, p):
    lis = []
    travel(m, '', set(p), 0, lis)
    # for place in p:
    #     print(place)
    #     remaining = set(p)
    #     remaining.remove(place)
    #     travel(m, place, remaining, 0, lis)
    #print(lis)
    print(max(lis))

m = {}
p = set()

f = open('d9i.txt')
text = f.read()
lines = text.splitlines()
for line in lines:
    parse_line(line, m, p)
print(m)
print(p)
disp(m, p)