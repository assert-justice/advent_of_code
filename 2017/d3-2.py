def board_gen(n):
    pos = (0,0,)
    val = 0
    board = {(0,0,): 1}
    dirs = [(1,0,), (0,-1,), (-1,0,), (0,1,)]
    diags = [(1,1,), (-1,1,), (-1,-1,), (1,-1)]
    didx = 0
    def add(a,b):
        return (a[0]+b[0],a[1]+b[1])
    def get_nei(pos):
        nei = 0
        for dir in dirs + diags:
            key = add(pos, dir)
            if key in board:
                nei += board[key]
        return nei
    while val <= n:
    #for i in range(10):
        #print(pos, i + 1)
        pos = add(pos, dirs[didx])
        pos1 = add(pos, dirs[didx])
        nei = get_nei(pos)
        nei1 = get_nei(pos1)
        if pos in board:
            # if we need a new ring
            didx = 0
            continue
        board[pos] = nei
        val = nei
        print(val)
        if nei1 == 0:
            # if we have overextended
            didx += 1
            if didx == 4:
                didx = 0
            
    print(board)

board_gen(277678)