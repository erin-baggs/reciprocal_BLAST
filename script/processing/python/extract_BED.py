#!/usr/bin/env python
import sys
import csv

from ktoolu_io import readFasta

def reverseComplement(seq, alphabet='ACGT'):
    """
    Returns the reverse complement of nucleic acid seqence input.
    """
    # compl = dict(zip(alphabet, alphabet[::-1]))
    compl= dict(zip('ACGTNRYWSMKBHDV', 'TGCANYRWSKMVDHB'))
    return ''.join([compl[base]
                    for base in seq.upper().replace('U', 'T')])[::-1]

sequences = dict()
with open(sys.argv[1]) as fi:
    for row in csv.reader(fi, delimiter='\t'): #changed from stdin to sys.argv
        if len(row) > 1:
            sequences[row[0]] = sequences.get(row[0], set())
            sequences[row[0]].add((int(row[1]), int(row[2]), "+", row[3]))
#print(sequences)

for _id, _seq in readFasta(sys.argv[2]):
    for start, end, strand, gid in sequences.get(_id[1:].split()[0], set()):
        tid = '>' + gid + '_%i-%i:%c' % (start, end, strand)
        tseq = _seq[start - 1: end]
        if strand == '-':
            tseq = reverseComplement(tseq)
        print(tid + '\n' + tseq)
