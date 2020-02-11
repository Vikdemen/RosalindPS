"""
For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2) is the ratio of the
total number of transitions to the total number of transversions, where symbol substitutions are inferred from
mismatched corresponding symbols as when calculating Hamming distance.
Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
Return: The transition/transversion ratio R(s1,s2).
"""

from typing import List

import rps.io_manager as io
import rps.sequences as seq


def main():
    fasta_sequences = io.read_file("input.txt")
    ratio = calculate_tt_ratio(fasta_sequences)
    print(round(ratio, 11))


def calculate_tt_ratio(fasta_sequences: List[str]) -> float:
    """
    :param fasta_sequences: Two equal length DNA sequences in FASTA format
    :return: Transition/transversion ratio
    """
    tagged_sequences = io.parse_fasta(fasta_sequences)
    first, second = [seq.DNA(sequence, tag) for sequence, tag in tagged_sequences]
    transitions, transversions = first.transitions_transversions(second)
    tt_ratio = transitions / transversions
    return tt_ratio


if __name__ == '__main__':
    main()
