import vd_bio_info

sequence = input("Enter the DNA sequence \n")
dna = vd_bio_info.DNA(sequence)
reverse_complement = dna.reverse_complement().sequence
print(reverse_complement)