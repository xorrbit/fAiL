#!/bin/sh

RUNS=5000000
N=6
TARGET='fail'
CHARS=$(expr $RUNS '*' $N)

LC_ALL=C tr -dc a-zA-Z0-9 < /dev/urandom \
    | head -c $CHARS \
    | fold -w $N \
    | grep -ni $TARGET \
    | sed -e 's/\(.*\):\(.*\)/hit: \2 pos: \1/g'
