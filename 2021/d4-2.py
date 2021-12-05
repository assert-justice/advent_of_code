from rich import print

def parse(lines):
    nums = lines[0].split(",")
    nums = [int(n) for n in nums]
    lines = lines[1:]
    boards = []
    idx = 0
    while idx < len(lines):
        idx += 1
        y = 0
        board = {}
        for _ in range(5):
            vals = lines[idx].split(" ")
            vals = filter(lambda val: len(val) > 0, vals)
            vals = [int(v) for v in vals]
            for x,n in enumerate(vals):
                key = (x,y,)
                board[n] = key
            idx += 1
            y += 1
        boards.append(board)
    return nums, boards

def board_sim(nums, board):
    coords = set()
    for idx, num in enumerate(nums):
        if num in board:
            new = board[num]
            coords.add(new)
            on_row = len(list(filter(lambda coord: coord[0] == new[0], coords)))
            on_col = len(list(filter(lambda coord: coord[1] == new[1], coords)))
            if on_row == 5 or on_col == 5:
                # win
                # score
                score = sum([n for n, coord in board.items() if not coord in coords])
                score *= num
                return idx + 1, score
    return None, 0

def play(lines):
    nums, boards = parse(lines)
    #print(nums, boards)
    #print(board_sim(nums, boards[2]))
    best = (0, 0)
    for board in boards:
        temp = board_sim(nums, board)
        print("temp:", temp)
        if temp[0] > best[0]:
            best = temp
    print(best)
f = open('2021/d4i.txt')
text = f.read()
lines = text.splitlines()
f.close()

#play(lines)
print(5 > None)