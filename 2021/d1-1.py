from rich import print

def numgen(ints):
    nums = []
    for i,n in enumerate(ints[:-2]):
        nums.append(n + ints[i+1] + ints[i+2])
    return nums

f = open('2021/d1i.txt')
text = f.read()
lines = text.splitlines()
f.close()
nums = [int(n) for n in lines]
nums = numgen(nums)
count = 0
for i,n in enumerate(nums):
    if i > 0:
        if n > nums[i-1]:
            count+=1
print(count)