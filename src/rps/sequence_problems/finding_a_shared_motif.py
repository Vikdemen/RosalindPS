"""
A common substring of a collection of strings is a substring of every member of the collection. We say that a
common substring is a longest common substring if there does not exist a longer common substring. For example,
"CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case,
"CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".
Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both
longest common substrings of "AACC" and "CCAA".
Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection.
(If multiple solutions exist, you may return any single solution.)
"""
from typing import List
from rps.sequence_problems.parsing import parse_fasta


def longest_substring(fasta_data: List[str]) -> str:
    """
    :param fasta_data: Several DNA sequences in FASTA format
    :return: Any of the longest substrings that are subsequences of every strand
    """
    strands = parse_fasta(fasta_data)
    sequences = [strand.sequence for strand in strands]

    # checks if substring is in all sequences
    def is_common(sub):
        for seq in sequences:
            if sub not in seq:
                return False
        else:
            return True

    # we assume that all nucleotides are present
    substrings = {'A', 'T', 'G', 'C'}

    # we make longer and longer substrings
    while True:
        longer = set()
        # for each substring we make longer variants
        for ss in substrings:
            variations = {'A' + ss, 'T' + ss, 'G' + ss, 'C' + ss, ss + 'A', ss + 'T', ss + 'G', ss + 'C'}
            variations = filter(is_common, variations)
            # and include ones that are still in all strings
            longer = longer.union(variations)
        # when we can't make substrings any longer
        if len(longer) == 0:
            # we get a random one from previous pool
            return substrings.pop()
        else:
            # and if we can, we use the new strings as new initial pool for variants
            substrings = longer
