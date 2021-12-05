def parse(nums):
    current = 0
    def node():
        nonlocal current
        #print(nums[current:current+2])
        child_count, meta_count = nums[current:current+2]
        current += 2
        children = [node() for _ in range(child_count)]
        meta = nums[current:current + meta_count]
        current += meta_count
        if child_count == 0:
            return sum(meta)
        total = 0
        print(meta, children)
        for idx in meta:
            if idx > 0 and idx < len(children):
                total += children[idx - 1]
        return total
    print(node())


f = open('2018/d8i.txt')
text = f.read()
f.close()
parse([int(n) for n in text.split(" ")])