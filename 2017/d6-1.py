def redis(banks:list):
    states = set()
    steps = 0
    while True:
        state = str(banks)
        if state in states:
            break
        steps += 1
        states.add(state)
        mx = max(banks)
        idx = banks.index(mx)
        banks[idx] = 0
        while mx > 0:
            idx += 1
            if idx == len(banks):
                idx = 0
            banks[idx] += 1
            mx -= 1
    print(steps)

redis([10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3,6])