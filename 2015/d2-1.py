f = open('d2i.txt')
text = f.read()
lines = text.split('\n')
boxes = [line.split('x') for line in lines]

def get_area(box):
    box = [int(side) for side in box]
    sides = [
        box[0] * box[1],
        box[1] * box[2],
        box[2] * box[0]
    ]
    return sum(sides) * 2 + min(sides)

print(sum([get_area(box) for box in boxes]))
f.close()