"""Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of
corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not
exceeding 1 kbp). Return: The Hamming distance dH(s,t).
"""
from typing import List

from rps.sequence_problems.sequences import DNA


def get_hamming_distance(sequences: List[str]) -> int:
    """
    :param sequences: Two sequences of equal length DNA strands
    :return: A number of mismatched nucleotides between them
    """
    if len(sequences) != 2:
        raise ValueError("There must be 2 sequences to compare")
    seq1, seq2 = sequences
    strand1 = DNA(seq1)
    strand2 = DNA(seq2)
    distance = strand1.calculate_hamming_distance(strand2)
    return distance
