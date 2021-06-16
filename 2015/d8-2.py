def char_count(line):
    val_count = 2
    i = 0
    while i < len(line):
        if line[i] == '"' or line[i] == '\\':
            val_count += 2
        else:
            val_count += 1
        i += 1
        # if line[i:i+2] == r'\x':
        #     i += 4
        #     val_count += 4 + 
        # if line[i:i+2] == r'\\':
        #     val_count += 1
        #     i += 2
        # elif line[i:i+2] == r'\"':
        #     val_count += 1
        #     i += 2
        # elif line[i:i+2] == r'\x':
        #     val_count += 1
        #     i += 4
        # elif line[i] == '"':
        #     i += 1
        # else:
        #     val_count += 1
        #     i += 1
    return val_count - len(line)

#print(char_count(r'"aaa\"aaa"'))

f = open('d8i.txt')
text = f.read()
lines = text.splitlines()
print(sum([char_count(line) for line in lines]))