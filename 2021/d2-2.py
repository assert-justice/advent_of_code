from rich import print

f = open('2021/d2i.txt')
text = f.read()
lines = text.splitlines()
f.close()

x = 0
depth = 0
aim = 0
for line in lines:
    order, amount = line.split(" ")
    amount = int(amount)
    if order == "forward":
        x += amount
        depth += amount * aim
    elif order == "down":
        aim += amount
    else:
        aim -= amount
print(x, depth, x * depth)