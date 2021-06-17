f = open('d3i.txt')
text = f.read()

v = set()
s1 = [0,0]
s2 = [0,0]
v.add(tuple(s1))
v.add(tuple(s2))

def move(c, s):
    if c == '>':
        s[0] += 1
    elif c == '<':
        s[0] -= 1
    elif c == '^':
        s[1] += 1
    else:
        s[1] -= 1
    print(s)
    v.add( tuple(s) )

for i, c in enumerate(text):
    #print(c)
    if i % 2 == 0:
        move(c, s1)
    else:
        move(c , s2)

print(len(v))