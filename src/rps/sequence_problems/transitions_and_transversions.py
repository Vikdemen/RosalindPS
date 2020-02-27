"""
For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2) is the ratio of the
total number of transitions to the total number of transversions, where symbol substitutions are inferred from
mismatched corresponding symbols as when calculating Hamming distance.
Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
Return: The transition/transversion ratio R(s1,s2).
"""

from typing import List

from rps.io_manager import as_fasta
from rps.sequence_problems.sequences import DNA


@as_fasta
def calculate_tt_ratio(strands: List[DNA]) -> float:
    """
    :param strands: Two equal length DNA strands
    :return: Transition/transversion ratio
    """
    first, second = strands
    transitions, transversions = first.transitions_transversions(second)
    tt_ratio = transitions / transversions
    return round(tt_ratio, 4)
