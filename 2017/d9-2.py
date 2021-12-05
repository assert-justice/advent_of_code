from typing import Counter


def parse(text):
    current = 0
    def advance():
        nonlocal current
        current += 1
        return text[current-1]
    def peek():
        return text[current]
    def garbage():
        # consume open angle bracket
        advance()
        chars = 0
        while True:
            c = peek()
            if c == '>':
                advance()
                return chars
            elif c == '!':
                advance()
                chars -= 1
            chars += 1
            advance()
    def group():
        total = 0
        # consume open curly brace
        advance()
        while True:
            # next char can be two things, a group or garbage
            c = peek()
            if c == '<': # if it's garbage consume it
                total += garbage()
            elif c == '{': # if it's a group call group and add it to the score. check for a comma suggesting more groups
                total += group()
            elif c == ',':
                advance()
            elif c == '}':
                advance()
                return total
            else:
                print("something went wrong!")
                return 0
    return group()

f = open('2017/d9i.txt')
text = f.read()
f.close()
print(parse(text))