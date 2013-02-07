import random
from string import ascii_letters, digits

RANGE_MAX = 5000000
CHARS_MAX = 6
ALPHANUM = ascii_letters + digits

for pos in range(0,RANGE_MAX):
    val = ''.join(random.choice(ALPHANUM) for x in range(CHARS_MAX))
    if 'fail' in val.lower():
        print "hit: %s pos: %s" % (val, pos)
