from itertools import permutations

def parse_line(line, rules, guests):
    line = line[:-1]
    line = line.split(' ')
    n1 = line[0]
    n2 = line[-1]
    guests.add(n1)
    guests.add(n2)
    d = int(line[3])
    if line[2] == 'lose':
        d = -d
    if not n1 in rules:
        rules[n1] = {}
    rules[n1][n2] = d

def eval_table(t_table, all_rules):
    table = list(t_table)
    table.append(table[0])
    table.append(table[1])
    #print(table)
    #print(table[1:-1])
    acc = 0
    for i, name in enumerate(table[1:-1]):
        rules = all_rules[name]
        n1 = table[i]
        n2 = table[i + 2]
        #print(name, n1, n2)
        if n1 in rules:
            acc += rules[n1]
        if n2 in rules:
            acc += rules[n2]
    #print(table[1:-1], acc)
    return acc

f = open('d13i.txt')
text = f.read()
lines = text.splitlines()
rules = {}
guests = set()
for line in lines:
    parse_line(line, rules, guests)
tables = permutations(guests)
print(max([eval_table(table, rules) for table in tables]))
# points = 0
# best_table = None
# for table in tables:
#     npoints = eval_table(table, rules) 
#     if npoints > points:
#         points = npoints
#         best_table = table
#eval_table( ('Bob', 'David', 'Alice', 'Carol',), rules )