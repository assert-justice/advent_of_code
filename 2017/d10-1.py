# def sim(leng, nums):
#     ls = [i for i in range(leng)]
#     skip = 0
#     start = 0
#     def inc(val):
#         val += 1
#         if val == leng:
#             val = 0
#         return val
#     for num in nums:
#         # grab front of list and reverse it
#         temp = []
#         idx = 0
#         for _ in range(num):
#             temp.append(ls[idx])
#             idx = inc(idx)
#         temp.reverse()
#         for _ in range(leng - num):
#             temp.append(ls[idx])
#             idx = inc(idx)
#         lskip = skip + num
#         print("start", ls)
#         ls = temp[lskip:] + temp[:lskip]
#         start += leng - lskip
#         skip += 1
#         print("temp", temp)
#         print("res", ls)
#         print(start, ls[start])
#         print()

def sim(leng, nums):
    def madd(val):
        return val % leng
    ls = [i for i in range(leng)]
    current = 0
    skip = 0
    for num in nums:
        print(ls)
        temp = []
        for i in range(num):
            temp.append(ls[madd(i + current)])
        temp.reverse()
        for i in range(num):
            ls[madd(i + current)] = temp[i]
        current += num + skip
        skip += 1
        print(ls)
        print()
    print(ls[0] * ls[1])

f = open('2017/d10i.txt')
text = f.read()
f.close()
nums = [int(num) for num in text.split(',')]
sim(256, nums)