def sim(leng, nums, rounds):
    def madd(val):
        return val % leng
    ls = [i for i in range(leng)]
    current = 0
    skip = 0
    for _ in range(rounds):
        for num in nums:
            temp = []
            for i in range(num):
                temp.append(ls[madd(i + current)])
            temp.reverse()
            for i in range(num):
                ls[madd(i + current)] = temp[i]
            current += num + skip
            skip += 1
    return ls

def read(s):
    nums = [ord(c) for c in s]
    nums += [17, 31, 73, 47, 23]
    return nums

def finish(ls):
    size = 16
    vals = []
    for i in range(size):
        group = ls[i * size: (i + 1) * size]
        val = 0
        for num in group:
            val ^= num
        vals.append(hex(val)[2:])
    return ''.join(vals)

f = open('2017/d10i.txt')
text = f.read()
f.close()
#nums = [int(num) for num in text.split(',')]
#sim(256, nums)
nums = read(text)
ls = sim(256, nums, 64)
print(finish(ls))