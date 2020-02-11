"""
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G',
and 'T' occur in s.
"""
from typing import Tuple
import rps.sequences as seq


def main():
    """
    Prints the counts of A, C, G, T
    """
    dna_sequence = input("Enter DNA sequence \n")
    counts = count_nucleotides(dna_sequence)
    print(counts)


def count_nucleotides(dna_sequence: str) -> Tuple[int, int, int, int]:
    """
    :param dna_sequence: A string represeting the sequence of nucleotides
    :return: Four integers - respective number of A, C, G and T nucleotides in input
    """
    dna_strand = seq.DNA(dna_sequence)
    counts = dna_strand.count_bases()
    return counts['A'], counts['C'], counts['G'], counts['T']


if __name__ == '__main__':
    main()
