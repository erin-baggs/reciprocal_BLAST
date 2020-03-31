#!/usr/bin/env python
# coding=utf-8

import sys
import csv
#import regular exprssion 

#fi= open(sys.argv[1])
#with open(sys.argv[1]) as fi:

def analyzeBlastResults(fi):
    nlr_co_ords = set()
    other_info = set()
    tig_name = set()

    for row in csv.reader(fi, delimiter='\t'):
        # print ('hello')
        if row[0].startswith('# Query'):
           tig_name='.'.join(row)
           continue


        elif row[0].startswith('#'):
            continue

        elif not row[0].startswith('#'):
            continue
        """
            rows= row[10], row[3], row[2]
            rows_2= row[0], row[10], row[3], row[2]
            _query = '.'.join(rows_2) #join needs one collection 
            geneid = row[0]
            evalue, alen, pid = map(float,(rows)) #float, (collection) #map useful when longer list so dont re-write assign. map from functional programming  
            if alen >= 1000 and pid >= 98 and evalue <= 1e-10: #: #not sure if this way to write evalue will work ??
                nlr_co_ords.add(_query)
        """                                                       
                                                                   # continue
    return tig_name

with open(sys.argv[1]) as fi:

    tig_name = analyzeBlastResults(fi)

for row  in tig_name:
    print row

    #list(map(str, your_list))
"""
        elif not row[0].startswith('#'):

            geneid, evalue, alen, pid = map(float, (row[0], row[10], row[3], row[2]))
            if alen >= 1000 and pid >= 98 and evalue <=0: #not sure if this way to write evalue will work ?? 
                nlr_co_ords.add(row[0], row[10], row[3], row[2])
                continue    
       # continue 

    return nlr_co_ords    
        
high_blast_match = analyzeBlastResults(sys.stdin)

for row in high_blast_match:
    print (row) 
"""
