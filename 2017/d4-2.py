def char_freq(word):
    cf = {}
    for c in word:
        if not c in cf:
            cf[c] = 0
        cf[c] += 1
    return cf
def compare_words(a, b):
    a = char_freq(a)
    b = char_freq(b)
    if len(a) != len(b):
        return False
    for c in a:
        if not c in b:
            return False
        if a[c] != b[c]:
            return False
    return True
def is_valid(line):
    words = line.split(' ')
    for i, w1 in enumerate(words):
        for f, w2 in enumerate(words):
            if i == f:
                continue
            if compare_words(w1,w2):
                return False
    return True

f = open('2017/d4i.txt')
text = f.read()
lines = text.splitlines()
f.close()

valid = 0
for line in lines:
    if is_valid(line):
        valid += 1
print(valid)