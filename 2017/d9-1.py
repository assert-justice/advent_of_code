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
        while True:
            c = peek()
            if c == '>':
                advance()
                return
            elif c == '!':
                advance()
            advance()
    def group(score):
        score += 1
        total = score
        # consume open curly brace
        advance()
        while True:
            # next char can be two things, a group or garbage
            c = peek()
            if c == '<': # if it's garbage consume it
                garbage()
            elif c == '{': # if it's a group call group and add it to the score. check for a comma suggesting more groups
                total += group(score)
            elif c == ',':
                advance()
            elif c == '}':
                advance()
                return total
            else:
                print("something went wrong!")
                return 0
    return group(0)

f = open('2017/d9i.txt')
text = f.read()
f.close()
print(parse(text))