def hash(leng, s, rounds):
    nums = [ord(c) for c in s]
    nums += [17, 31, 73, 47, 23]
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
    size = 16
    vals = []
    for i in range(size):
        group = ls[i * size: (i + 1) * size]
        val = 0
        for num in group:
            val ^= num
        num = bin(val)[2:]
        num = (8 - len(num)) * '0' + num
        #print(num)
        vals.append(num)
    return ''.join(vals)

def solve(key):
    count = 0
    for i in range(128):
        h = hash(256, key + '-' + str(i), 1)
        for c in h:
            if c == '1':
                count += 1
    print(count)

solve('flqrgnkx')