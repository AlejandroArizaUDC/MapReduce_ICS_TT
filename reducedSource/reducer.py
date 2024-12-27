#!/usr/bin/env python

import sys

console_sales = {}

developer_scores = {}

na_genre_sales = {}
jp_genre_sales = {}
other_genre_sales = {}


for line in sys.stdin:
    line = line.strip()

    _, console, genre, developer, critic_score, total_sales, na_sales, jp_sales, other_sales = line.split('\t')

    total_sales = float(total_sales) if total_sales != 'N/A' else 0.0


    try:
        genre = genre if genre != 'N/A' else None
    except ValueError:
        critic_score = None

    try:
        na_sales = float(na_sales) if na_sales != 'N/A' else 0.0
    except ValueError:
        na_sales = 0.0

    try:
        jp_sales = float(jp_sales) if jp_sales != 'N/A' else 0.0
    except ValueError:
        jp_sales = 0.0

    try:
        other_sales = float(other_sales) if other_sales != 'N/A' else 0.0
    except ValueError:
        other_sales = 0.0


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


    if genre is not None:
        if genre in na_genre_sales:
            na_genre_sales[genre] += na_sales
        else:
            na_genre_sales[genre] = na_sales
            
    if genre is not None:
        if genre in jp_genre_sales:
            jp_genre_sales[genre] += jp_sales
        else:
            jp_genre_sales[genre] = jp_sales

    if genre is not None:
        if genre in other_genre_sales:
            other_genre_sales[genre] += other_sales
        else:
            other_genre_sales[genre] = other_sales


for console, sales in console_sales.items():
    print '%s\t%.2f' % (console, sales)



print "\n\nPuntuaciones desarrolladoras:\n"

for developer, scores in developer_scores.items():
    if scores: 
        average_score = sum(scores) / len(scores)
        print '%s\t%.2f' % (developer, average_score)


print "\nGeneros mas populares por region:\n"


if na_genre_sales:
    na_most_popular_genre = max(na_genre_sales, key=na_genre_sales.get)
    print 'NA: %s\t%.2f' % (na_most_popular_genre, na_genre_sales[na_most_popular_genre])


if jp_genre_sales:
    jp_most_popular_genre = max(jp_genre_sales, key=jp_genre_sales.get)
    print 'JP: %s\t%.2f' % (jp_most_popular_genre, jp_genre_sales[jp_most_popular_genre])


if other_genre_sales:
    other_most_popular_genre = max(other_genre_sales, key=other_genre_sales.get)
    print 'Other: %s\t%.2f' % (other_most_popular_genre, other_genre_sales[other_most_popular_genre])

