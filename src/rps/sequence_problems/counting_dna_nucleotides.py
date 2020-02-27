"""
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G',
and 'T' occur in s.
"""
from typing import Tuple, List
from rps.sequence_problems.sequences import DNA


def main():
    """
    Prints the counts of A, C, G, T
    """
    dna_sequence = input("Enter DNA sequence \n")
    counts = count_nucleotides(dna_sequence)
    print(counts)
    # TODO - fix list vs str


def count_nucleotides(dna_sequences: List[str]) -> Tuple[int, int, int, int]:
    """
    :param dna_sequences: A list of strings represeting the sequence of nucleotides
    :return: Four integers - respective number of A, C, G and T nucleotides in input
    """
    for seq in dna_sequences:
        seq.strip('/n')
    dna_sequence = ''.join(dna_sequences)
    dna_strand = DNA(dna_sequence)
    counts = dna_strand.count_bases()
    return counts['A'], counts['C'], counts['G'], counts['T']


if __name__ == '__main__':
    main()
