"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist,
then you may return any one of them.)
"""
from typing import List
from rps.io_manager import as_fasta
from rps.sequence_problems.sequences import DNA
from collections import namedtuple

ProfileMatrix = namedtuple('ProfileMatrix', ['A', 'T', 'G', 'C'])


def get_profile_matrix(strands: List[DNA]):
    """
    The profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth
    position of one of the strings, P2,j represents the number of times that C occurs in the jth position,
    and so on.
    :return:
    """
    sequence_length = len(strands[0].sequence)
    # checks that sequences are of the same length
    if any((len(strand.sequence) != sequence_length for strand in strands)):
        raise ValueError("Sequences must be of same length")
    # list of counts are initially filled with zeros
    matrix = ProfileMatrix(
        [0 for _ in range(sequence_length)],
        [0 for _ in range(sequence_length)],
        [0 for _ in range(sequence_length)],
        [0 for _ in range(sequence_length)]
    )
    for strand in strands:
        for i, base in enumerate(strand.sequence):
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


@as_fasta
def get_consensus_and_matrix(sequences: List[DNA]):
    profile_matrix = get_profile_matrix(sequences)
    consensus_string = get_consensus_string(profile_matrix)
    matrix_representation = '\n'.join(f"{base}: {getattr(profile_matrix, base)}" for base in ['A', 'T', 'G', 'C'])
    return consensus_string, '/n', matrix_representation
