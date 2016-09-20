<<<<<<< HEAD
#!/usr/bin/env python3
from Bio.Seq import Seq
from Bio.Alphabet import generic_rna


seq = input().strip()
seq = Seq(seq,generic_rna)
prot = seq.translate()
print(prot[:len(prot)-1])
=======
#!/usr/bin/env python3
from Bio.Seq import Seq
from Bio.Alphabet import generic_rna


seq = input().strip()
seq = Seq(seq,generic_rna)
prot = seq.translate()
print(prot[:len(prot)-1])
>>>>>>> abfe9e0c9413d6f3f3d7498ab1b806d822fb81f8
