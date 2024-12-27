#!/usr/bin/env python

import sys
import random


first_line = True

for line in sys.stdin:
    line = line.strip()
    if first_line: 
        first_line = False
        continue
    fields = line.split(',')


    random_key = random.randint(0, 1)

    fields = [field if field else 'N/A' for field in fields]

    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (random_key, fields[2],fields[3],fields[5], fields[6],fields[7], fields[8], fields[10], fields[11])