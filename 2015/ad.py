import sys

d = sys.argv[1]
inp = 'd{}i.txt'.format(d)
t = 'f = open(\'{}\')\ntext = f.read()\n\n'.format(inp)
open('d{}-1.py'.format(d), 'w').write(t)
open('d{}-2.py'.format(d), 'w').write(t)
open(inp, 'w')