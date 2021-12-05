def count(s):
    total = 0
    for idx,c in enumerate(s):
        idx += len(s) // 2
        if idx >= len(s):
            idx -= len(s)
        if c == s[idx]:
            total += int(c)
    print(total)

f = open('2017/d1i.txt')
text = f.read()
count(text)
f.close()