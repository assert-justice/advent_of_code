import json

def is_dict(obj):
    return type(obj) == type({})

def is_list(obj):
    return type(obj) == type([])

def is_string(obj):
    return type(obj) == type('')

def ex(obj):
    if is_dict(obj):
        if 'red' in obj.values():
            return 0
        return sum([ ex(value) for value in obj.values()])
    elif is_list(obj):
        return sum([ex(value) for value in obj])
    elif is_string(obj):
        return 0
    else:
        return obj

f = open('d12i.txt')
text = f.read()
j = json.loads(text)
print(ex(j))