"""
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the
exons to form a new string ready for translation.
Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings
are given in FASTA format.
Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will
exist for the dataset provided.)
"""
from typing import List
import rps.io_manager as io
import rps.sequence_problems.sequences as seq


def main():
    fasta_sequences = io.read_file("input.txt")
    protein_sequence = splice_and_translate(fasta_sequences)
    print(protein_sequence)


def splice_and_translate(fasta_sequences: List[str]) -> str:
    """
    :param fasta_sequences: A DNA sequence of gene in FASTA format, followed by several intron sequences
    :return: A protein sequence obtained after translating spliced RNA
    """
    # parses the fasta format
    tagged_sequences = io.parse_fasta(fasta_sequences)
    rna_strands = [seq.DNA(sequence, tag).transcribe() for sequence, tag in tagged_sequences]
    # sequence_problems are DNA, so we need to transcribe them
    matrix = rna_strands[0]
    introns = rna_strands[1:]
    # split matrix RNA and introns
    for intron in introns:
        matrix = matrix.splice(intron)
    # we need protein sequence from spliced RNA
    protein = matrix.translate_to_protein()
    return protein.sequence


if __name__ == '__main__':
    main()
