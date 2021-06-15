f = open('d5i.txt')
text = f.read()

def has_vowels(s):
    v = 'aeiou'
    s = [c for c in s if c in v]
    return len(s) > 2

def has_repeat(s):
    lc = ''
    for c in s:
        if c == lc:
            return True
        lc = c
    return False

def no_bad_substr(s):
    bad = ['ab', 'cd', 'pq', 'xy']
    for b in bad:
        if b in s:
            return False
    return True

#print(has_vowels('jchzalrnumimnmhp'))
nice = 0
for line in text.splitlines():
    if has_vowels(line) and has_repeat(line) and no_bad_substr(line):
        nice += 1
print(nice)