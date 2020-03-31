#!/usr/bin/env python

#use: python <script> <XMLtoParse> <long_outfile> <short_outfile>

import sys
from Bio.Blast import NCBIXML
#Usage, opens an outfile and then parses any number of .xml files into that outfile, printing all hits
#parse_blastn.py outfile.txt anynumberofinfiles.xml
recorded=dict()
OUT = open(sys.argv[2], 'w')
OUT2 = open(sys.argv[3],'w')
OUT.write("Sbjct Chromosome\tSbjct Start\tSbjct end\tQuery\n")
for i in sys.argv[1]:
    result_handle = open(sys.argv[1])
    blast_records = NCBIXML.parse(result_handle)
    for rec in blast_records:
        #print(rec.title)
        for alignment in rec.alignments: #using NCBIXML to loop through individual alignments  
            #print(alignment)
            for hsp in alignment.hsps: #using NCBIXML to pull info on hsps
                #print(hsp)
                fields = [ alignment.accession,str(hsp.sbjct_start), str(hsp.sbjct_end), str(rec.query)]
                OUT.write("\t".join(fields) + "\n") #writing to outfile 1 each individual HSP bed co-ord 
                query=str(fields[3:4])
                if query in recorded: #This part takes recorded hsps and combines then to the general region coords
                    #print('query')
                    raw_chromo_fields=str(fields[0:1]) #Here we are identifying if HSPS are on same chromo
                    edit_chromo_fields=raw_chromo_fields.split("'")[1]
                    #print(edit_chromo_fields)
                    raw_rec_chr=str(recorded[query][0:1])
                    edit_rec_chr=raw_rec_chr.split("'")[1]
                    #print(edit_rec_chr)
                    if edit_chromo_fields==edit_rec_chr: #use key of query to get chromo ID 
                        #print(fields[1:2])
                        edit_strt_chromo=str(fields[1:2]).split("'")[1] #Here we are preparing the data to be comparable 
                        edit_stp_chromo=str(fields[2:3]).split("'")[1]
                        edit_strt_rec1=str(recorded[query][1:2]).split("[")[1]
                        edit_strt_rec=str(edit_strt_rec1).split("]")[0]
                        edit_stp_rec1=str(recorded[query][2:3]).split("[")[1]
                        edit_stp_rec=str(edit_stp_rec1).split("]")[0]
                        edit_strt_rec=edit_strt_rec.strip("'")
                        edit_stp_rec=edit_stp_rec.strip("'")
                        chr_strt=int(edit_strt_chromo)
                        chr_stp=int(edit_stp_chromo)
                        rec_strt=int(edit_strt_rec)
                        rec_stp=int(edit_stp_rec)
                        if chr_strt > chr_stp: # Here we are checking the orientation of genomic co-ord
                            tmp_stp=chr_strt
                            chr_strt=chr_stp
                            chr_stp=tmp_stp
                            #print(tmp_stp)
                        if rec_strt > chr_strt : #Here we ask if the the new alignment starts before current recorded start
                            if (rec_strt - chr_strt) <= 3000:
                            #print('alternate start')
                            #print(edit_strt_chromo)
                            #print('original_start')
                            #print(recorded[query][1])
                                recorded[query][1]=edit_strt_chromo
                                #print(recorded)
                        if rec_stp < chr_stp: #Here we ask if the new alignment stop is after the current recorded stop 
                            if (chr_stp - rec_stp) <=3000:      
                                recorded[query][2]=edit_stp_chromo
                                #print(recorded)

                else: #here we are recording the first entry for that record 
                    start=(str(fields[1:2]).split("'")[1])
                    stop=(str(fields[2:3]).split("'")[1])
                    start=int(start)
                    stop=int(stop)
                    chromo=(str(fields[0:1]).split("'")[1])
                    if start < stop:
                        recorded[query]=[chromo,start,stop]
                    else:
                        recorded[query]=[chromo,stop,start]
                    #print(recorded)
OUT.close()


for k,v in recorded.items(): #here we are printing the combined bed region per alignment to second outfile 
    strl="\t"
    strung=(strl.join([str(elem) for elem in v]))
    qid=str(k.split("'")[1])  
    OUT2.write(strung+"\t"+qid+"\n")

OUT2.close()

#print(query) 
#ask for chromom - is chromo the same if no add to dict if yes move on to ask for start and end co-ord if new field start and stop within or within 1000bp of dict then extend given co-ord 

