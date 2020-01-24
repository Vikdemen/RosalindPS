import VDBioinfo

sequence = input("Enter the DNA sequence \n")
dna = VDBioinfo.DNA(sequence)
reverse_complement = dna.reverse_complement().sequence
print(reverse_complement)