'''
given a number and the following spiral pattern, find the x and y coordinates of that number
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
one is at (0,0)
loop one has 8 nums
loop len = (flr(loop/2) + 1) * 4 + 4
nine is at (1,1)
loop two has 
num len next
1   8   9
2   
loop_len n -> n * 8
'''
def solve(n):
    c = 0
    for i in range(n):
        c += i * 8
        #print((i,i,), c + 1 )
        if c + 1 >= n:
            quad_leng = i * 2
            quad = c + 1 - n
            q = quad // quad_leng
            off = quad % quad_leng
            if q == 0:
                return (i-off, i,)
            elif q == 1:
                return (-i,i-off,)
            elif q == 2:
                return (-i+off,-i)
            else:
                return (i, -i+off)
def man_dis(co):
    return abs(co[0]) + abs(co[1])

co = solve(277678)
print(man_dis(co))
