def parse_line(line):
    line = line.split(' ')
    rd = {
        'name': line[0],
        'speed': int(line[3]),
        'dur': int(line[6]),
        'rest': int(line[13]),
        'x': 0,
        'points': 0,
        'resting': True,
        'time': 0
    }
    return rd

# def simulate(rd, time):
#     x = 0
#     resting = False
#     while time > 0:
#         if resting:
#             time -= rd['rest']
#             resting = False
#         elif rd['dur'] > time:
#             time = 0
#             x += time * rd['speed']
#         else:
#             x += rd['speed'] * rd['dur']
#             time -= rd['dur']
#             resting = True
#     print(rd['name'], x)
#     return x

def simulate(rds):
    first = []
    biggest_x = 0
    for rd in rds:
        if rd['time'] == 0:
            rd['resting'] = not rd['resting']
            if rd['resting']:
                rd['time'] = rd['rest']
            else:
                rd['time'] = rd['dur']
        if not rd['resting']:
            rd['x'] += rd['speed']
        rd['time'] -= 1
        if rd['x'] > biggest_x:
            biggest_x = rd['x']
            first = [rd]
        elif rd['x'] == biggest_x:
            first.append(rd)
    for rd in first:
        rd['points'] += 1

# rd = parse_line('Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.')
# simulate(rd, 1000)

f = open('d14i.txt')
text = f.read()
lines = text.splitlines()
rds = [parse_line(line) for line in lines]
for i in range(2503):
    simulate(rds)
for rd in rds:
    print(rd)
print(max([rd['points'] for rd in rds]))