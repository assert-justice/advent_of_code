'''
cubic coordinate system
track x, y, and z coords
origin is (0,0,0)
north / south is x
ne / sw is y
nw / se is z

n: (0,1,-1)
ne: (1,0,-1)
se: (1,-1,0)
s: (0,-1,1)
sw: (-1,0,1)
nw: (-1,1,0)

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \
'''

def sim(steps):
    dirs = {
        'n': (0,1,-1),
        'ne': (1,0,-1),
        'se': (1,-1,0),
        's': (0,-1,1),
        'sw': (-1,0,1),
        'nw': (-1,1,0),
    }
    pos = [0,0,0]
    def move(step):
        dir = dirs[step]
        for i in range(3):
            pos[i] += dir[i]
    for step in steps:
        move(step)
    return pos

def dis(pos):
    #(abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z)) / 2
    return (abs(pos[0]) + abs(pos[1]) + abs(pos[2])) // 2

f = open('2017/d11i.txt')
text = f.read()
f.close()
steps = text.split(',')
pos = sim(steps)
print(dis(pos))