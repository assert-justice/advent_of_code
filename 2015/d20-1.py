import math

def score(n):
    s = n * 10
    ns = int(math.sqrt(n))
    for i in range(1, ns + 1):
        if n % i == 0:
            s += i * 10
            if n != 1 and n // i > i:
                s += n // i * 10
    return s

# print(score(1500000))

num = 33_100_000

# for i in range(1, 1_000_000):
#     if score(i) >= num:
#         print(i)
#         break
print(score(6))