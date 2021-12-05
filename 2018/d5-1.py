def react(s):
    for idx, c in enumerate(s[:-1]):
        char : str = s[idx+1]
        if c.lower() == char.lower() and c != char:
            return ''.join(s.split(c+char))
f = open('2018/d5i.txt')
text = f.read()
last = ''
while text:
    last = text
    text = react(text)
    #print(text)
print(len(last))