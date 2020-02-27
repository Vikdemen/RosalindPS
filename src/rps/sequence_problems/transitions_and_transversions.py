"""
For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2) is the ratio of the
total number of transitions to the total number of transversions, where symbol substitutions are inferred from
mismatched corresponding symbols as when calculating Hamming distance.
Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
Return: The transition/transversion ratio R(s1,s2).
"""

from typing import List

from rps.io_manager import parse_fasta


def calculate_tt_ratio(fasta_data: List[str]) -> float:
    """
    :param fasta_data: Two equal length DNA sequences in FASTA format
    :return: Transition/transversion ratio, rounded to 4th digit
    """
    strands = parse_fasta(fasta_data)
    first, second = strands
    transitions, transversions = first.transitions_transversions(second)
    tt_ratio = transitions / transversions
    return round(tt_ratio, 4)
