"""
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For
example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same
GC-content.
DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling
is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some
labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the
label of the next string.
In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx"
denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind
allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on
absolute error below.
"""
from typing import List, Tuple
from parsing import parse_fasta


def calculate_max_gc_content(fasta_data: List[str]) -> Tuple[str, float]:
    """
    :param fasta_data: - a list of DNA sequences in FASTA format
    :return: the tag and gc content of DNA strand with highest GC content
    """
    strands = parse_fasta(fasta_data)
    gc_content_values = [(strand.tag, strand.gc_content()) for strand in strands]
    max_tag, max_gc_content = max(gc_content_values, key=lambda value: value[1])
    return max_tag, max_gc_content
