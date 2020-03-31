#!/usr/bin/env python
# coding=utf-8

import sys
import csv
#script <monocot_athal_blast> <dicot_athal_blast> 
with open(sys.argv[1]) as fi_P1:
    P1 = set() #Present 1 - Athal ortholog genes present in monocots
    P2 = set() #Present 2 - Athal ortholog genes present in monocots and dicots
    for row in csv.reader(fi_P1, delimiter=' '):
        if "hits" in row:
            if (float(row[1])) > 0 :
                blast_result = fi_P1.next()
                GID_Athal_long= blast_result.split()[1]
                GID_Athal= GID_Athal_long.split('.')[0]
                P1.add(GID_Athal)
        else:
            continue

with open(sys.argv[2]) as fi_P2:
    for row in csv.reader(fi_P2, delimiter=' '):
        if "hits" in row:
            if (float(row[1])) > 0 :
                blast_result_dicot = fi_P2.next()
                GID_Athal_long_2= blast_result_dicot.split()[1]
                GID_Athal_2= GID_Athal_long_2.split('.')[0]
                if GID_Athal_2 in P1: # Should be last P? list
                    P2.add(GID_Athal_2)
        else:
            continue

for i in P2:
    print (i)
