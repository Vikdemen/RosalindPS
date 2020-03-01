"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the
complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
Given: A DNA string s of length at
most 1000 bp.
Return: The reverse complement sc of s.
"""
from typing import List
from rps.sequence_problems.sequences import DNA


def complement_dna(lines: List[str]) -> str:
    """
    :param lines: A line with DNA sequence
    :return: Reversed RNA sequence
    """
    # only one sequence is expected
    dna_sequence, = lines
    dna = DNA(dna_sequence)
    reverse_complement = dna.reverse_complement()
    return reverse_complement.sequence
