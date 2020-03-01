"""
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G',
and 'T' occur in s.
"""
from typing import List
from rps.sequence_problems.sequences import DNA


def count_nucleotides(lines: List[str]) -> str:
    """
    :param lines: A line, in a list representing DNA sequence
    :return: Four numbers separated by spaces - respective number of A, C, G and T nucleotides in input
    """
    # only one sequence is expected
    dna_sequence, = lines
    dna_strand = DNA(dna_sequence)
    counts = dna_strand.count_bases()
    return f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}"
