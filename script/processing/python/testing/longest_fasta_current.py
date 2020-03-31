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
    gid = pid
    #print(pid) #debug
    if pid.split('.') == True:
        gid = pid.split('.')[0]
    #print(gid) #debug
    if gid not in gene:
        #gene[gid] = {}
        gene[gid] = [pid, len(_seq), _seq]
    if float(gene[gid][1]) < len(_seq):
        #print (float(gene[gid][1]))
        #print (_seq)
        gene[gid] = [pid, len(_seq), _seq]
        #print(gid)
        #print (gene[gid]) #debug
#print (gene)

for _id, _seq in readFasta(sys.argv[1]):
    pid = _id.split()[0]
    gid = pid
    if pid.split('.') == True:
        gid = pid.split('.')[0]
    #print(pid) #debug
    if gid not in seen:
        #print ('in loop') #debug
        seen.add(gid) 
        #if gid in gene: 
        print(gene[gid][0])
        print(gene[gid][2])
#print(seen)
