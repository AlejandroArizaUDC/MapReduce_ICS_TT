#!/usr/bin/env python

import sys

console_sales = {}

for line in sys.stdin:
    line = line.strip()

    _, console, genre, developer, critic_score, total_sales, na_sales, jp_sales, other_sales = line.split('\t')

    total_sales = float(total_sales) if total_sales != 'N/A' else 0.0

    if console in console_sales:
        console_sales[console] += total_sales
    else:
        console_sales[console] = total_sales

for console, sales in console_sales.items():
    print '%s\t%.2f' % (console, sales)
    