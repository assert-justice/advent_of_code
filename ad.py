import sys

y = sys.argv[1]
d = sys.argv[2]
t = f'''
with open('{y}/d{d}i.txt') as f:
    text = f.read()
    lines = text.splitlines()
'''

with open(f'{y}/d{d}-1.py') as f:
    f.write(t)
with open(f'{y}/d{d}-2.py') as f:
    f.write(t)
with open(f'{y}/d{d}i.txt') as f:
    f.write("")
#t = 'from rich import print\n\nf = open(\'{}\')\ntext = f.read()\nf.close()\n\nlines = text.splitlines()'.format(inp)
# open('{}/d{}-1.py'.format(y, d), 'w').write(t)
# open('{}/d{}-2.py'.format(y, d), 'w').write(t)
# open(inp, 'w')