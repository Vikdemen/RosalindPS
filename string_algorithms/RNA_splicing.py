from typing import List

import rps_io_manager as file
import rps_sequences as seq


def main():
    fasta_sequences = file.read_file("input.txt")
    protein_sequence = splice_and_translate(fasta_sequences)
    print(protein_sequence)


def splice_and_translate(fasta_sequences: List[str]) -> str:
    # parses the fasta format
    tagged_sequences = file.parse_fasta(fasta_sequences)
    rna_strands = [seq.DNA(sequence, tag).transcribe() for sequence, tag in tagged_sequences]
    # sequences are DNA, so we need to transcribe them
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
