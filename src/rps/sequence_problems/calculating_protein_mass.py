"""
In a weighted alphabet, every symbol is assigned a positive real number called a weight. A string formed from
a weighted alphabet is called a weighted string, and its weight is equal to the sum of the weights of its symbols.
The standard weight assigned to each member of the 20-symbol amino acid alphabet is the monoisotopic mass of
the corresponding amino acid.
Given: A protein string P of length at most 1000 aa.
Return: The total weight of P. Consult the monoisotopic mass table.
"""
from typing import List

import rps.sequence_problems.sequences as seq


def calculate_mass(lines: List[str]) -> str:
    """
    :param lines: a sequence of aminoacids in the form of the string using 1-letter notation
    :return: Monoisotopic mass of peptide chain with a given sequence of residues
    """
    # only one sequence is expected
    peptide_sequence, = lines
    peptide = seq.Peptide(peptide_sequence)
    mass = peptide.calculate_mass()
    return f"{mass:.4f}"
