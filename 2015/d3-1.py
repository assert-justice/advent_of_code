f = open('d3i.txt')
text = f.read()

x = 0
y = 0
v = {(x,y,): 1}
print(v)

def add_house():
    key = (x,y,)
    if key in v:
        v[key] += 1
    else:
        v[key] =1

for c in  text:
    if c == '>':
        x += 1
    elif c == '<':
        x -= 1
    elif c == '^':
        y += 1
    else:
        y -= 1
    add_house()

print(len(v))