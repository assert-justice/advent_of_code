def parse(nums):
    current = 0
    acc = []
    def node():
        nonlocal current
        nonlocal acc
        child_count, meta = nums[current:current+2]
        current += 2
        #children = [node() for _ in range(child_count)]
        for _ in range(child_count):
            node()
        acc += nums[current:current + meta]
        current += meta
    node()
    print(sum(acc))


f = open('2018/d8i.txt')
text = f.read()
f.close()
parse([int(n) for n in text.split(" ")])