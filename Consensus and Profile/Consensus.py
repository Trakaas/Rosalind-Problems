#!/usr/bin/env python3
from Bio import SeqIO
from Bio import Seq
from Bio.Alphabet import generic_dna

reads = list(SeqIO.parse('rosalind_cons.txt','fasta',generic_dna))
reads = [item for item in reads]

consensus = {'A':[0]*len(reads[0]),'C':[0]*len(reads[0]),'G':[0]*len(reads[0]),'T':[0]*len(reads[0])}
c_strand=['']*len(reads[0])

for x in range(0,len(reads[0])):
    consensus['A'][x] = len([item[x] for item in reads if item[x] =='A'])
    consensus['C'][x] = len([item[x] for item in reads if item[x] =='C'])
    consensus['G'][x] = len([item[x] for item in reads if item[x] =='G'])
    consensus['T'][x] = len([item[x] for item in reads if item[x] =='T'])
    c_strand[x] = [key for key in sorted(consensus) if consensus[key][x] == max([consensus['A'][x],consensus['C'][x],consensus['G'][x],consensus['T'][x]])]

c_strand = [item for sublist in c_strand for item in sublist]

print('  ',' '.join(c_strand))
for key in sorted(consensus):
    print(key+':',' '.join(str(x) for x in consensus[key]))
