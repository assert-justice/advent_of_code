def parse_line(line):
    line = line.split(' ')
    rd = {
        'name': line[0],
        'speed': int(line[3]),
        'dur': int(line[6]),
        'rest': int(line[13]),
    }
    return rd

def simulate(rd, time):
    x = 0
    resting = False
    while time > 0:
        if resting:
            time -= rd['rest']
            resting = False
        elif rd['dur'] > time:
            time = 0
            x += time * rd['speed']
        else:
            x += rd['speed'] * rd['dur']
            time -= rd['dur']
            resting = True
    print(rd['name'], x)
    return x



# rd = parse_line('Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.')
# simulate(rd, 1000)

f = open('d14i.txt')
text = f.read()
lines = text.splitlines()
rds = [parse_line(line) for line in lines]
print(max([simulate(rd, 2503) for rd in rds]))