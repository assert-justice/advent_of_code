import itertools

def parse_line(line, ings):
    name = line[:line.find(':')]
    line = line[len(name) + 1:].split(',')
    #line = [ing.strip().split(' ') for ing in line]
    ingred = {}
    for ing in line:
        ing = ing.strip().split(' ')
        if ing[0] == 'calories':
            continue
        ingred[ing[0]] = int(ing[1])
    ings[name] = ingred

def score(ings: dict, r):
    count = {}
    for ingred in r:
        quant = r[ingred]
        ing = ings[ingred]
        for prop in ing:
            if not prop in count:
                count[prop] = 0
            count[prop] += ing[prop] * quant
    s = 1
    for prop in count:
        if count[prop] < 0:
            return 0
        s *= count[prop]
    #print(s)
    return s

def get_combos(i_ings, scoops):
    rs = []
    def combo(ings, scoops, lis):
        if len(ings) == 1:
            lis.append(scoops)
            r = {}
            for i in range(len(i_ings)):
                r[i_ings[i]] = lis[i]
            rs.append(r)
            #print(lis)
            return
        after = ings[1:]
        #print(after)
        for i in range(1, scoops - len(after) + 1):
            ls = lis[:]
            ls.append(i)
            combo(after, scoops - i, ls)
    combo(i_ings[:], scoops, [])
    #print(len(rs))
    return rs

f = open('d15i.txt')
text = f.read()
lines = text.splitlines()

ings = {}
for line in lines:
    parse_line(line, ings)
# print(ings)
# r1 = {'Butterscotch': 44, 'Cinnamon': 56}
# print(score(ings, r1))
#r2 = {'Butterscotch': 62, 'Cinnamon': 38}
#print(score(ings, r2))

combos = get_combos(list(ings.keys()), 100)
print(max([score(ings, combo) for combo in combos]))
# best_r = None
# best_score = 0
# for r in combos:
#     ns = score(ings, r)
#     if ns > best_score:
#         best_score = ns
#         best_r = r
# print(best_r)
# r = {
#     'Butterscotch': 44,
#     'Cinnamon': 56
# }
# score(ings, r)