import sys

y = sys.argv[1]
d = sys.argv[2]
inp = '{}/d{}i.txt'.format(y, d)
t = 'from rich import print\n\nf = open(\'{}\')\ntext = f.read()\nlines = text.splitlines()\nf.close()\n'.format(inp)
open('{}/d{}-1.py'.format(y, d), 'w').write(t)
open('{}/d{}-2.py'.format(y, d), 'w').write(t)
open(inp, 'w')