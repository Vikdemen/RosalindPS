from typing import List, Set
from rps.io_manager import parse_fasta, read_file
from rps.sequence_problems.sequences import DNA


def get_possible_proteins(fasta_sequence: List[str]) -> Set[str]:
    tagged_sequences = parse_fasta(fasta_sequence)
    # there should be only one sequence
    assert len(tagged_sequences) == 1
    sequence, tag = tagged_sequences[0]
    strand = DNA(sequence, tag)
    orfs = strand.search_for_orf()
    proteins = {orf.transcribe().translate_to_protein().sequence for orf in orfs}
    return proteins


def main():
    fasta_sequences = read_file("input.txt")
    proteins = get_possible_proteins(fasta_sequences)
    for protein in proteins:
        print(protein)


if __name__ == '__main__':
    main()
