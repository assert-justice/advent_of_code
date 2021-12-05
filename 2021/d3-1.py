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
gamma = [c / len(lines) > 0.5 for c in counts]
epsilon = [not c for c in gamma]
gamma = "0b" + "".join([str(int(c)) for c in gamma])
epsilon = "0b" + "".join([str(int(c)) for c in epsilon])
print(len(lines))
print(counts)
print(gamma)
print(epsilon)
print(int(gamma, 2) * int(epsilon, 2))