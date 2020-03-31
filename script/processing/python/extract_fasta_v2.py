#!/usr/bin/env python
# coding=utf-8
import sys 
import glob
import re

import pandas as pd

from Bio import Entrez
from Bio import SeqIO
from Bio.Blast import NCBIXML

'''
The parse_hits() function will read the BLAST output XML file, 
extract the genome and protein id to further extract the protein record
description and sequence from the genome FASTA file.
'''

def parse_hits(f):
    result_handle=open(f)
    blast_record = NCBIXML.read(result_handle)
    
    # Split file path to extract protein name and use the path
    # and protein to create the new FASTA file
    f=str(f)
    #prot = f.split("'")[1]
    prot= f.split('_')[0]
    new_fasta = open(prot+'_blast.fasta', 'w')
    #print(new_fasta)
     
    # Count records
    rec = 0

    # Loop through the XML file
    for alignment in blast_record.alignments:
        
        # Record genome and protein ID and incearse the count
        genome = alignment.title.split(' ')[-1]
        ref_no = alignment.title.split(' ',2)[1]
        rec += 1
        
        # Open genome FASTA file and find the original sequence
        # and description for the record and write it to the 
        # new FASTA file containing all matches
        file = prot+'.fasta'
        for seq_record in SeqIO.parse(file, 'fasta'):
            if ref_no in seq_record.description:
                new_fasta.write('>'+str(seq_record.description))
                new_fasta.write('\n')
                new_fasta.write(str(seq_record.seq))
                new_fasta.write('\n')

    result_handle.close()
    new_fasta.close()
 
    print(prot,'\t',rec)

fi = sys.argv[1]
parse_hits(fi)

