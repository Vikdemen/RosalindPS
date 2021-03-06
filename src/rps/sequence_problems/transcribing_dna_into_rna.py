"""
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all
occurrences of 'T' in t with 'U' in u.
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""
from typing import List

import rps.sequence_problems.sequences as seq


def transcribe(lines: List[str]) -> str:
    """
    :param lines: A list with a line with DNA sequence to be transcribed
    :return: Transcribed non-reversed sequence with T replaced with U
    """
    # only one sequence expected
    dna_sequence, = lines
    dna = seq.DNA(dna_sequence)
    rna = dna.transcribe()
    return rna.sequence
