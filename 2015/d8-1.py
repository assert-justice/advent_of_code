def char_count(line):
    val_count =0
    i = 0
    while i < len(line):
        if line[i:i+2] == r'\\':
            val_count += 1
            i += 2
        elif line[i:i+2] == r'\"':
            val_count += 1
            i += 2
        elif line[i:i+2] == r'\x':
            val_count += 1
            i += 4
        elif line[i] == '"':
            i += 1
        else:
            val_count += 1
            i += 1
    return len(line) - val_count

#print(char_count(r'"\x27"'))

f = open('d8i.txt')
text = f.read()
lines = text.splitlines()
print(sum([char_count(line) for line in lines]))