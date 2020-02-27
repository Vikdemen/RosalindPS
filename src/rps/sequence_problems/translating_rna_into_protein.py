"""
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters
except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic
string will incorporate protein strings along with DNA strings and RNA strings.
The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.
"""
from typing import List

import rps.sequence_problems.sequences as seq


def translate_dna(lines: List[str]) -> str:
    # only one is expected
    sequence, = lines
    rna = seq.RNA(sequence)
    protein = rna.translate_to_protein()
    return protein.sequence
