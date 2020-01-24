import VDBioinfo

my_sequence = input("Enter DNA sequence \n")
dna = VDBioinfo.DNA(my_sequence)
counts = dna.count_bases()
print(counts)