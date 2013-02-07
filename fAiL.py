import numpy.random as random
import re
from string import ascii_letters, digits

RANGE_MAX = xrange(0, 5000000)
CHARS_MAX = range(6)
ALPHANUM = list(ascii_letters + digits)
ALPHANUM_LENGTH = len(ALPHANUM)
TARGET = 'fail'

for pos in RANGE_MAX:
    val = ''
    for x in CHARS_MAX:
        val += ALPHANUM[random.randint(0, ALPHANUM_LENGTH)]
    if TARGET in val.lower():
        print "hit: %s pos: %s" % (val, pos)
