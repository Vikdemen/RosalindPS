from typing import Tuple

import rps.sequences as seq

"""
Counts every nucleotide in given DNA sequence, then prints counts of A, C, G, T
"""


def main():
    dna_sequence = input("Enter DNA sequence \n")
    counts = count_nucleotides(dna_sequence)
    print(counts)


def count_nucleotides(dna_sequence: str) -> Tuple[int, int, int, int]:
    dna_strand = seq.DNA(dna_sequence)
    counts = dna_strand.count_bases()
    return counts['A'], counts['C'], counts['G'], counts['T']


if __name__ == '__main__':
    main()
