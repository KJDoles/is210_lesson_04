#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Uses lists and loops to track account transactions.
'''

import data
print data.TRANSACTIONS

TOTAL = 0
for list in data.TRANSACTIONS:
    for int in list:
        TOTAL = TOTAL + int

MINIMUM = None
for day in data.TRANSACTIONS:
    DAY_TOT = 0
    for amount in day:
        DAY_TOT = DAY_TOT + amount
    if MINIMUM == None:
        MINIMUM = DAY_TOT
    elif DAY_TOT < MINIMUM:
        MINIMUM = DAY_TOT

MAXIMUM = None
for day in data.TRANSACTIONS:
    DAY_TOT = 0
    for amount in day:
        DAY_TOT = DAY_TOT + amount
    if MAXIMUM == None:
        MAXIMUM = DAY_TOT
    elif DAY_TOT > MAXIMUM:
        MAXIMUM = DAY_TOT
