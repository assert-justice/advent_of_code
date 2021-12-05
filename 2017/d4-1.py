def is_valid(line):
    line = line.split(' ')
    s = set(line)
    return len(line) == len(s)

f = open('2017/d4i.txt')
text = f.read()
lines = text.splitlines()
f.close()

valid = 0
for line in lines:
    if is_valid(line):
        valid += 1
print(valid)