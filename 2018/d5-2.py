def react(s):
    for idx, c in enumerate(s[:-1]):
        char : str = s[idx+1]
        if c.lower() == char.lower() and c != char:
            return ''.join(s.split(c+char))
def collapse(text):
    last = ''
    while text:
        last = text
        text = react(text)
        #print(text)
    return last
def remove(s : str, c : str):
    s = ''.join(s.split(c))
    c = c.upper()
    return ''.join(s.split(c))
def solve(text):
    al = 'abcdefghijklmnopqrstuvwxyz'
    best_c = ''
    best_l = len(text)
    for c in al:
        s = remove(text, c)
        l = len(collapse(s))
        print(c, l)
        if l < best_l:
            best_l = l
            best_c = c
    print('best', best_c, best_l)
    
f = open('2018/d5i.txt')
text = f.read()
solve(text)