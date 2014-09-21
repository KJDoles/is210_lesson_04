#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Uses for loop to return 4 measurements of data.SHAKESPEARE.
'''

import data
print data.SHAKESPEARE
SHAKES = data.SHAKESPEARE.split('\n')
MAXIMUM_WORDS = 0
MINIMUM_WORDS = len(SHAKES[0].split())

for line in SHAKES:
    WORDS = line.split()
    if len(WORDS)> MAXIMUM_WORDS:
        MAXIMUM_WORDS = len(WORDS)

for line in SHAKES:
    WORDS = line.split()
    if len(WORDS)< MINIMUM_WORDS:
        MINIMUM_WORDS = len(WORDS)

NUM_LINES = 0
NUM_WORDS = 0
for line in SHAKES:
    NUM_LINES += 1
    NUM_WORDS += len(line.split())

AVERAGE_WORDS = float(NUM_WORDS) / float(NUM_LINES)

NUM_CRISPIAN = 0
for line in SHAKES:
    if 'Crispian' in line:
        NUM_CRISPIAN = NUM_CRISPIAN + 1



    

