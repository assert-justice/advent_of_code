def sim(last, fact):
    return last * fact % 2147483647

def compare(a, b):
    a = bin(a)
    b = bin(b)
    print(a, "\n", b)
    return a[:-16] == b[:-16]

a = 65
b = 8921
gen_a_factor = 16807
gen_b_factor = 48271
compare(a, b)