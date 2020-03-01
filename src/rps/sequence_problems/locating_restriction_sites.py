"""
A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse
palindrome because its reverse complement is GCATGC. See Figure 2.
Given: A DNA string of length at most 1 kbp in FASTA format.
Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may
return these pairs in any order.
"""
from typing import List
from rps.sequence_problems.parsing import parse_fasta


def palindrome_positions(fasta_data: List[str]) -> str:
    """
    :param fasta_data: DNA sequence in FASTA format
    :return: Pairs of position and length of every reverse palindrome in sequence with length 4-12 in random order
    """
    dna_strand, = parse_fasta(fasta_data)
    min_length = 4
    max_length = 12
    palindromes = dna_strand.find_reverse_palindromes(min_length, max_length)
    formatted_pairs = [f"{position} {length}" for position, length in palindromes]
    return '\n'.join(formatted_pairs)
