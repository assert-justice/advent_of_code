def find_divs(nums):
    for x in nums:
        for y in nums:
            if x == y:
                continue
            if x // y == x / y:
                print(x, y)
                return x // y
def csum(lines):
    cs = 0
    for line in lines:
        line = line.split('\t')
        line = sorted([int(n) for n in line])
        print(line)
        cs += find_divs(line)
    print(cs)

f = open('2017/d2i.txt')
text = f.read()
lines = text.splitlines()
csum(lines)
f.close()