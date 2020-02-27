"""
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the
exons to form a new string ready for translation.
Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings
are given in FASTA format.
Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will
exist for the dataset provided.)
"""
from typing import List
from rps.io_manager import parse_fasta


def splice_and_translate(fasta_data: List[str]) -> str:
    """
    :param fasta_data: A DNA sequence of gene, followed by several intron sequences, in FASTA format
    :return: A protein sequence obtained after translating spliced RNA
    """
    dna_strands = parse_fasta(fasta_data)
    # sequences are DNA, so we need to transcribe them
    rna_strands = [strand.transcribe() for strand in dna_strands]
    # first sequence is
    matrix, *introns = rna_strands
    for intron in introns:
        matrix = matrix.splice(intron)
    # we need protein sequence from spliced RNA
    protein = matrix.translate_to_protein()
    return protein.sequence
