import sys
import fileinput
from collections import defaultdict, Counter
from itertools import permutations

out = defaultdict(lambda: Counter())

# precache all the ranks
ranks = defaultdict(lambda: dict())

for line in fileinput.input(sys.argv[1:]):
    files = line.split()
    changeset = files.pop(0)
    if len(files) > 100: # somewhat arbitrary
        continue

    for f in files:
        out[f][f]  # set them to 0 if needs be.

    for (p1,p2) in permutations(files,2):
        out[p1][p2] += 1

    if len(files) == 1:
        f = files[0]
        out[f][f] += 1  # solo pairing!


# loop once to fill ranks.
for (p1) in (out):
    for (ii,(p2,c)) in enumerate(out[p1].most_common()):
        ranks[p1][p2] = ii  #

for (p1) in (out):
    for (p2,c) in (out[p1].iteritems()):
        r1 = ranks[p1][p2]
        r2 = ranks[p2][p1]
        print "\t".join([p1,p2,str(c), ['-', "self"][int(p1 == p2)], str(r1), str(r2), ['-', "<3"][r1==r2==1] ])



# ideas.... ranks....
# 1 vs #1


