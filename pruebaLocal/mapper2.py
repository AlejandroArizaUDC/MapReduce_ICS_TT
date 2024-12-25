#!/usr/bin/env python3

import sys
import random

first_line = True

for line in sys.stdin:
    line = line.strip()
    if first_line:  # Ignorar la primera línea
        first_line = False
        continue

    # Dividir los campos por comas, que es lo esperado en este caso
    fields = line.split(',')

    # Generar una clave aleatoria
    random_key = random.randint(0, 1)

    # Reemplazar valores vacíos con 'N/A'
    fields = [field if field else 'N/A' for field in fields]

    # Imprimir el resultado con formato
    print('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (
        random_key, fields[2], fields[3], fields[5], fields[6], fields[7], fields[8], fields[10], fields[11]
    ))
