"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist,
then you may return any one of them.)
"""
from typing import List
import rps.io_manager as io
from collections import namedtuple


ProfileMatrix = namedtuple('ProfileMatrix', ['A', 'T', 'G', 'C'])


def get_profile_matrix(sequences: List[str]):
    """
    The profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth
    position of one of the strings, P2,j represents the number of times that C occurs in the jth position,
    and so on.
    :return:
    """
    sequence_length = len(sequences[0])
    # checks that sequences are of the same length
    assert all((len(seq) == sequence_length for seq in sequences))
    # list of counts are initially filled with zeros
    matrix = ProfileMatrix(
        [0 for _ in range(sequence_length)],
        [0 for _ in range(sequence_length)],
        [0 for _ in range(sequence_length)],
        [0 for _ in range(sequence_length)]
    )
    for sequence in sequences:
        for i, base in enumerate(sequence):
            getattr(matrix, base)[i] += 1
    return matrix


def get_consensus_string(matrix: ProfileMatrix) -> str:
    bases = ['A', 'T', 'G', 'C']
    consensus = []
    for counts in zip(matrix.A, matrix.T, matrix.G, matrix.C):
        tagged_values = zip(bases, counts)
        most_common_base, best_count = max(tagged_values, key=lambda v: v[1])
        consensus.append(most_common_base)
    consensus = ''.join(consensus)
    return consensus


def main():
    unparsed = io.read_file("input.txt")
    parsed = io.parse_fasta(unparsed)
    sequences = [sequence[0] for sequence in parsed]
    profile_matrix = get_profile_matrix(sequences)
    consensus_string = get_consensus_string(profile_matrix)
    print(consensus_string)
    for base in ['A', 'C', 'G', 'T']:
        print(f"{base}:", *getattr(profile_matrix, base))


if __name__ == '__main__':
    main()
