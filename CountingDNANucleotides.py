import vd_bio_info

my_sequence = input("Enter DNA sequence \n")
dna = vd_bio_info.DNA(my_sequence)
counts = dna.count_bases()
print(counts)