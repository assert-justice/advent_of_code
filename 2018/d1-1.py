f = open('2018/d1i.txt')
text = f.read()
lines = text.splitlines()

def main():
    count = 0
    d = set()
    while True:
        for line in lines:
            count += int(line)
            if count in d:
                print(count)
                return
            d.add(count)
    print(count)
    print(d)
main()