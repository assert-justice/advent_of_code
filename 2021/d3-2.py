from rich import print

f = open('2021/d3i.txt')
text = f.read()
lines = text.splitlines()
f.close()

counts = [0 for _ in lines[0]]
for line in lines:
    for idx, c in enumerate(line):
        if c == '1':
            counts[idx] += 1
print(counts)
gamma = [c / len(lines) > 0.5 for c in counts]
epsilon = [not c for c in gamma]
gamma = [int(c) for c in gamma]
epsilon = [int(c) for c in epsilon]

def get_gamma(arr):
    counts = [0 for _ in arr[0]]
    for line in arr:
        for idx, c in enumerate(line):
            if c:
                counts[idx] += 1
    return [int(c / len(arr) >= 0.5) for c in counts]

def filt(lines, neg, debug = False):
    num_arrs = []
    for line in lines:
        num_arrs.append([int(c) for c in line])
    ln = len(lines[0])
    for idx in range(ln):
        pattern = get_gamma(num_arrs)
        if neg:
            pattern = [not c for c in pattern]
        num_arrs = list(filter(lambda arr: arr[idx] == pattern[idx], num_arrs))
        if debug:
            print("filter", idx, pattern[idx])
            print(num_arrs)
        #print(num_arrs)
        if len(num_arrs) == 1:
            return num_arrs[0]

def to_num(arr):
    return int("0b" + "".join([str(c) for c in arr]), 2)

#print(gamma)
print(gamma)
a = to_num(filt(lines, False))
b = to_num(filt(lines, True))
print(a, b, a * b)