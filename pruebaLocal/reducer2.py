#!/usr/bin/env python3

import sys

console_sales = {}

for line in sys.stdin:
    line = line.strip()

    # Dividir las columnas del input
    _, console, genre, developer, critic_score, total_sales, na_sales, jp_sales, other_sales = line.split('\t')

    # Convertir total_sales a float, reemplazando 'N/A' por 0.0
    total_sales = float(total_sales) if total_sales != 'N/A' else 0.0

    # Acumular las ventas por consola
    if console in console_sales:
        console_sales[console] += total_sales
    else:
        console_sales[console] = total_sales

# Imprimir las ventas totales por consola
for console, sales in console_sales.items():
    print('%s\t%.2f' % (console, sales))
