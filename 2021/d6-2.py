from rich import print
# time: 19 minutes
# beaten by: 1989

def tally(group, num, count = 1):
    if not num in group:
        group[num] = 0
    group[num] += count
def group_fish(fish):
    g = {}
    for f in fish:
        tally(g, f)
    return g
def sim(groups):
    temp = {}
    for group, num in groups.items():
        group -= 1
        if group == -1:
            group = 6
            tally(temp, 8, num)
        tally(temp, group, num)
    return temp

f = open('2021/d6i.txt')
text = f.read()
f.close()
nums = [int(c) for c in text.split(",")]
nums = group_fish(nums)
for _ in range(4):
    print("go")
    for _ in range(64):
        nums = sim(nums)
print(nums)
num = sum(nums.values())
print(num)