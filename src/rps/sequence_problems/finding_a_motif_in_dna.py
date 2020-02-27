"""
Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
Above, we use 1-based numbering, as opposed to 0-based numbering, which is used in Python.
"""
from typing import List
from rps.sequence_problems.sequences import DNA


def get_motif_positions(sequences: List[str]) -> List[int]:
    """
    :param sequences: Two sequences - main sequence and motif to search for
    :return: A list of 1-based positions of motif inside the sequence
    """
    main_sequence, motif = sequences
    strand = DNA(main_sequence)
    positions = strand.search_for_motif(motif)
    return positions
