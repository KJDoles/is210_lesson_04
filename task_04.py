#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Divides list of names into four teams with a maximum of four people.
Disregards people with a bad connection.
'''

import data
TEAM1 = ()
TEAM2 = ()
TEAM3 = ()
PLAYAS = data.MULTIPLAYERS.split('\n')
PLAYA_HATR = PLAYAS[1:]

NUM_NAME = 0
for line in PLAYA_HATR:
    while NUM_NAME <= 12:
        NAME = line.split()
        if NAME[-1] == 0:
            continue
        elif NAME != 0:
            TEAM1 = TEAM1 + NAME
            NUM_NAME += 1
    
    
