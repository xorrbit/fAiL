import random
from string import ascii_letters, digits

RANGE_MAX = xrange(0, 5000000)
CHARS_MAX = range(6)
ALPHANUM = ascii_letters + digits
TARGET = 'fail'

for pos in RANGE_MAX:
    val = ''
    for x in CHARS_MAX:
        val += random.choice(ALPHANUM)
    if TARGET in val.lower():
        print "hit: %s pos: %s" % (val, pos)
