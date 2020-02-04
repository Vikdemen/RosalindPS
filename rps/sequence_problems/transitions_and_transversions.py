from typing import List

import rps.io_manager as io
import rps.sequences as seq


def main():
    fasta_sequences = io.read_file("input.txt")
    ratio = calculate_tt_ratio(fasta_sequences)
    print(round(ratio, 11))


def calculate_tt_ratio(fasta_sequences: List[str]) -> float:
    tagged_sequences = io.parse_fasta(fasta_sequences)
    first, second = [seq.DNA(sequence, tag) for sequence, tag in tagged_sequences]
    transitions, transversions = first.transitions_transversions(second)
    tt_ratio = transitions / transversions
    return tt_ratio


if __name__ == '__main__':
    main()
