#!/usr/bin/env python

import sys
from Bio.Blast import NCBIXML
#Usage, opens an outfile and then parses any number of .xml files into that outfile, printing all hits
#parse_blastn.py outfile.txt anynumberofinfiles.xml

OUT = open(sys.argv[1], 'w')
OUT.write("Sbjct Chromosome\tSbjct Start\tSbjct end\tQuery\n")
for xml_file in sys.argv[2:]:
    result_handle = open(xml_file)
    blast_records = NCBIXML.parse(result_handle)
    for rec in blast_records:
        #print(rec.title)
        for alignment in rec.alignments:
            #print(alignment)
            for hsp in alignment.hsps:
                #print(hsp)
                fields = [ alignment.accession,str(hsp.sbjct_start), str(hsp.sbjct_end), str(rec.query)]
                OUT.write("\t".join(fields) + "\n")
OUT.close()
