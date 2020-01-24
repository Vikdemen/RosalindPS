import VDBioinfo

sequence = input("Enter DNA sequence \n")
dna = VDBioinfo.DNA(sequence)
rna = dna.transcribe()
print(rna.sequence)