f = open('i1.txt')
text = f.read()
floor = 0
for i, c in enumerate(text):
    if c == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(i + 1)
        break