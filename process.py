import sys
import fileinput
from collections import defaultdict, Counter
from itertools import permutations

out = defaultdict(lambda: Counter())
for line in fileinput.input(sys.argv[1:]):
    files = line.split()
    changeset = files.pop(0)
    if len(files) > 20: # somewhat arbitrary
        continue

    for f in files:
        out[f][f]  # set them to 0 if needs be.

    for (p1,p2) in permutations(files,2):
        out[p1][p2] += 1

    if len(files) == 1:
        f = files[0]
        out[f][f] += 1  # solo pairing!


for (p1) in (out):
    for (p2,c) in (out[p1].iteritems()):
        print "\t".join([p1,p2,str(c), "*" * int(p1 == p2)])




