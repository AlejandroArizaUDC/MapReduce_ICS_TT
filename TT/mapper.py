#!/usr/bin/env python

import sys
import random

for line in sys.stdin:
    line = line.strip()
    fields = line.split()


    random_key = random.randint(0, 1)

    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (random_key, fields[2],fields[3],fields[5], fields[6],fields[7], fields[8], fields[10])