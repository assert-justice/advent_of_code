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

def get_length(box):
    box = [int(side) for side in box]
    perims = [
        (box[0] + box[1]) * 2,
        (box[1] + box[2]) * 2,
        (box[2] + box[0]) * 2
    ]
    return min(perims) + box[0] * box[1] * box[2]

print(sum([get_length(box) for box in boxes]))
f.close()