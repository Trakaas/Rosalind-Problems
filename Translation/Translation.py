#!/usr/bin/env python3
from Bio.Seq import Seq
from Bio.Alphabet import generic_rna


seq = input().strip()
seq = Seq(seq,generic_rna)
prot = seq.translate()
print(prot[:len(prot)-1])
