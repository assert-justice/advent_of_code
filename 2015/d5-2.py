f = open('d5i.txt')
text = f.read()

lines = text.splitlines()

def r1(s):
    for i in range(len(s) - 1):
        ss = s[i:i+2]
        if s.find(ss, i+2) != -1:
            return True
    return False

def r2(s):
    for i in range(len(s) - 3):
        print(s[i] + s[i+1] + s[i+2])
        if s[i] == s[i + 2]:
            return True
    return False

#print(r2('aaab'))

nice = 0
for line in lines:
    if r1(line) and r2(line):
        nice += 1
print(nice)