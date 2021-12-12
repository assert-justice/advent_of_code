import sys

y = sys.argv[1]
d = sys.argv[2]
inp = '{}/d{}i.txt'.format(y, d)
t = 'from rich import print\n\nf = open(\'{}\')\ntext = f.read()\nf.close()\n\nlines = text.splitlines()'.format(inp)
open('{}/d{}-1.py'.format(y, d), 'w').write(t)
open('{}/d{}-2.py'.format(y, d), 'w').write(t)
open(inp, 'w')