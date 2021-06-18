f = open('2015/d1i.txt')
text = f.read()
floor = 0
for c in text:
    if c == '(':
        floor += 1
    else:
        floor -= 1
print(floor)