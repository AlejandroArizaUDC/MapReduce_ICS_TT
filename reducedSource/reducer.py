#!/usr/bin/env python

import sys

console_sales = {}

developer_scores = {}

for line in sys.stdin:
    line = line.strip()

    _, console, genre, developer, critic_score, total_sales, na_sales, jp_sales, other_sales = line.split('\t')

    total_sales = float(total_sales) if total_sales != 'N/A' else 0.0

    try:
        critic_score = float(critic_score) if critic_score != 'N/A' else None
    except ValueError:
        critic_score = None

    if console in console_sales:
        console_sales[console] += total_sales
    else:
        console_sales[console] = total_sales


    if critic_score is not None:
        if developer not in developer_scores:
            developer_scores[developer] = []  
        developer_scores[developer].append(critic_score)



for console, sales in console_sales.items():
    print '%s\t%.2f' % (console, sales)



print "\n\nPuntuaciones desarrolladoras:\n"

for developer, scores in developer_scores.items():
    if scores: 
        average_score = sum(scores) / len(scores)
        print '%s\t%.2f' % (developer, average_score)