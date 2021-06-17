def encode_password(password):
    return [ord(c) - ord('a') for c in password]

def decode_password(code):
    print(''.join([chr(c + ord('a')) for c in code]))

def inc_code(code):
    for i in range(1, len(code)):
        code[-i] += 1
        if code[-i] == 26:
            code[-i] = 0
        else:
            break
    return code

prohib = [ord(c) - ord('a') for c in 'iol']
def no_prohib(code):
    for p in prohib:
        if p in code:
            return False
    return True

def found_straight(code):
    for i in range(len(code) - 2):
        if code[i] == code[i + 1] - 1 and code[i] == code[i + 2] - 2:
            return True
    return False

def found_pairs(code):
    pairs = set()
    for i in range(len(code) - 1):
        if code[i] == code[i+1]:
            pairs.add( (code[i],code[i + 1],) )
    return len(pairs) > 1

code = encode_password('hxbxxyzz')
while True:
    code = inc_code(code)
    if no_prohib(code) and found_straight(code) and found_pairs(code):
        break
decode_password(code)
# code = encode_password('ghijllaa')
# print(no_prohib(code))
# print(found_pairs(code))
# print(found_straight(code))