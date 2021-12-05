def char_freq(s):
    freq = {}
    for c in s:
        if not c in freq:
            freq[c] = 0
        freq[c] += 1
    return freq

def solve(lines):
    threes = 0
    twos = 0
    for line in lines:
        freq : dict = char_freq(line)
        if 3 in freq.values():
            threes += 1
        if 2 in freq.values():
            twos += 1
    print(threes * twos)

f = open('2018/d2i.txt')
text = f.read()
lines = text.splitlines()

solve(lines)