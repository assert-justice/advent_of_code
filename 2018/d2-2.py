def dist(s1, s2):
    dis = 0
    char = ''
    for idx, c in enumerate(s1):
        if c != s2[idx]:
            char = c
            dis += 1
    return dis, char

def solve(lines):
    seen = []
    for line in lines:
        for entry in seen:
            d, char = dist(line, entry)
            if(d == 1):
                print(line, entry, char)
                return
        seen.append(line)

f = open('2018/d2i.txt')
text = f.read()
lines = text.splitlines()

solve(lines)