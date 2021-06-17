def look_and_say(line):
    line = 'a' + line
    counts = []
    i = 1
    while i < len(line):
        if line[i] != line[i-1]:
            counts.append([])
        counts[-1].append(line[i])
        i += 1
    return ''.join([str(len(count)) + str(count[0]) for count in counts])

line = '1321131112'
for i in range(50):
    line = look_and_say(line)
print(len(line))