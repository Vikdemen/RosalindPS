import rps.io_manager as io
import rps.sequence_problems.consensus_and_profile as problem

dataset = [
    ">Rosalind_1",
    "ATCCAGCT",
    ">Rosalind_2",
    "GGGCAACT",
    ">Rosalind_3",
    "ATGGATCT",
    ">Rosalind_4",
    "AAGCAACC",
    ">Rosalind_5",
    "TTGGAACT",
    ">Rosalind_6",
    "ATGCCATT",
    ">Rosalind_7",
    "ATGGCACT"
]

parsed = io.parse_fasta(dataset)
sequences = [sequence[0] for sequence in parsed]


def test_get_profile_matrix():
    result = problem.get_profile_matrix(sequences)
    expected_matrix = {
        'A': [5, 1, 0, 0, 5, 5, 0, 0],
        'C': [0, 0, 1, 4, 2, 0, 6, 1],
        'G': [1, 1, 6, 3, 0, 1, 0, 0],
        'T': [1, 5, 0, 0, 0, 1, 1, 6]
    }
    assert result == expected_matrix


def test_get_consensus_string():
    matrix = problem.get_profile_matrix(sequences)
    result = problem.get_consensus_string(matrix)
    expected_string = 'ATGCAACT'
    assert result == expected_string
