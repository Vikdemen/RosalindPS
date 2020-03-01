"""
Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA
string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids:
three reading frames result from reading the string itself, whereas three more result from reading its reverse
complement.
An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop
codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids
until a stop codon is reached.
Given: A DNA string s of length at most 1 kbp in FASTA format.
Return: Every distinct candidate protein string that can be translated from ORFs of s.
Strings can be returned in any order.
"""
from typing import List
from rps.sequence_problems.parsing import parse_fasta


def get_possible_proteins(fasta_data: List[str]) -> str:
    """
    :param fasta_data: A DNA sequence in FASTA format
    :return: a formatted set of possible proteins encoded in DNA
    """
    strands = parse_fasta(fasta_data)
    # there should be only one sequence
    strand, = strands
    orfs = strand.search_for_orf()
    proteins = {orf.transcribe().translate_to_protein().sequence for orf in orfs}
    return '\n'.join(proteins)
