from rich import print

def sim(fish):
    new_fish = []
    def m(fish):
        fish -= 1
        if fish == -1:
            new_fish.append(8)
            fish = 6
        return fish
    fish = list(map(m, fish))
    return fish + new_fish

f = open('2021/d6i.txt')
text = f.read()
f.close()
nums = [int(c) for c in text.split(",")]
for _ in range(80):
    nums = sim(nums)
print(len(nums))