#!/usr/bin/env python
import sys

"""
gene['AT4G']={}
>>> gene['AT4G']['AT4G.2']=13
"""
gene = {}
seen = set() 
from ktoolu_io import readFasta
for _id, _seq in readFasta(sys.argv[1]):
    pid = _id.split()[0]
    #print(pid) #debug
    gid = pid.split('.')[-1]
    #print(gid) #debug
    if gid not in gene:
        gene[gid]={}
        gene[gid] = [pid, len(_seq), _seq]
    if float(gene[gid][1]) < len(_seq):
        #print (float(gene[gid][1]))
        #print (_seq)
        gene[gid] = [pid, len(_seq), _seq]
        #print(gid)
        #print (gene[gid]) #debug

for _id, _seq in readFasta(sys.argv[1]):
    pid = _id.split()[0]
    #print(pid) #debug
    gid = pid.rsplit('.')[0]
    if gid not in seen:
        seen.add(gid) 
        if gid in gene: 
            print(gene[gid][0])
            print(gene[gid][2])
