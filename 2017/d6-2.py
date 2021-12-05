def redis(banks:list):
    states = {}
    steps = 0
    while True:
        state = str(banks)
        if state in states:
            print(steps - states[state])
            break
        states[state] = steps
        steps += 1
        mx = max(banks)
        idx = banks.index(mx)
        banks[idx] = 0
        while mx > 0:
            idx += 1
            if idx == len(banks):
                idx = 0
            banks[idx] += 1
            mx -= 1


#arr = [2, 4, 1, 2]
arr = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3,6]
redis(arr)