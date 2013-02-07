import random
from string import ascii_letters, digits

RANGE_MAX = xrange(0, 5000000)
CHARS_MAX = range(6)
ALPHANUM = ascii_letters + digits

for pos in RANGE_MAX:
    val = ''.join(random.choice(ALPHANUM) for x in CHARS_MAX)
    if 'fail' in val.lower():
        print "hit: %s pos: %s" % (val, pos)
