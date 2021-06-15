import hashlib
#print(hashlib.md5(b'abcdef609043').digest().hex())

def test(n):
    secret = 'iwrupvqb'
    #secret = 'abcdef'
    val = (secret + str(n)).encode('utf-8')
    val = hashlib.md5(val).digest().hex()
    return val[:6] == '000000'

# print(test(609042))
for i in range(1_000_000_000):
    if test(i):
        print(i)
        break