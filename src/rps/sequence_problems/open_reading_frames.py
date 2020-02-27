from typing import List
from parsing import parse_fasta


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
