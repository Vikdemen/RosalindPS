import vd_bio_info

sequence = input("Enter DNA sequence \n")
dna = vd_bio_info.DNA(sequence)
rna = dna.transcribe()
print(rna.sequence)