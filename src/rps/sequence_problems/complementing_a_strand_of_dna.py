"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the
complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC"). Given: A DNA string s of length at
most 1000 bp. Return: The reverse complement sc of s.
"""
from rps.io_manager import single_line
from rps.sequence_problems.sequences import DNA


@single_line
def complement_dna(dna_sequence: str) -> str:
    """
    :param dna_sequence: a string of ATGC
    :return: str, reversed RNA sequence
    """
    dna = DNA(dna_sequence)
    reverse_complement = dna.reverse_complement()
    return reverse_complement.sequence
