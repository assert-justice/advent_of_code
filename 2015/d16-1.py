def is_match(aunt, line):
    name = line[:line.find(':')]
    line = line[len(name) + 1:].split(',')
    #print(name)
    for prop in line:
        prop = prop.split(':')
        prop_name = prop[0].strip()
        prop_val = int(prop[1])
        #print(prop_name, prop_val)
        if aunt[prop_name] != prop_val:
            return
    print("It's " + name)

aunt = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

f = open('d16i.txt')
text = f.read()
lines = text.splitlines()
for line in lines:
    is_match(aunt, line)
    