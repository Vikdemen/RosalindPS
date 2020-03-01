"""
A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns.
Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in
which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents
the number of times that C occurs in the jth position, and so on.

A consensus string c is a string of length n formed from our collection by taking the most common symbol at each
position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the
profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus
strings.
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist,
then you may return any one of them.)
"""
from typing import List
from rps.sequence_problems.parsing import parse_fasta
from rps.sequence_problems.sequences import DNA
from collections import namedtuple

ProfileMatrix = namedtuple('ProfileMatrix', ['A', 'T', 'G', 'C'])


def get_profile_matrix(strands: List[DNA]) -> ProfileMatrix:
    """
        The profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth
    position of one of the strings, P2,j represents the number of times that C occurs in the jth position,
    and so on.
    :param strands: Several DNA strands of equal length
    :return: A profile matrix for these strands
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
    """
        A consensus string c is a string of length n formed from our collection by taking the most common symbol at each
    position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of
    the profile matrix. There may be more than one most common symbol, leading to multiple possible consensus strings.
    :param matrix: Profile matrix of several sequences
    :return: Random consensus string of that matrix
    """
    bases = ['A', 'T', 'G', 'C']
    consensus = []
    for counts in zip(matrix.A, matrix.T, matrix.G, matrix.C):
        tagged_values = zip(bases, counts)
        most_common_base, best_count = max(tagged_values, key=lambda v: v[1])
        consensus.append(most_common_base)
    consensus = ''.join(consensus)
    return consensus


def get_consensus_and_matrix(fasta_data: List[str]) -> str:
    strands = parse_fasta(fasta_data)
    profile_matrix = get_profile_matrix(strands)
    consensus_string = get_consensus_string(profile_matrix)
    matrix_representation = '\n'.join(f"{base}: {getattr(profile_matrix, base)}" for base in ['A', 'T', 'G', 'C'])
    return f"{consensus_string}'/n{matrix_representation}"
