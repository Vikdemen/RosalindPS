from src.rps.sequence_problems.parsing import parse_fasta
import src.rps.sequence_problems.consensus_and_profile as problem

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

sequences = parse_fasta(dataset)


def test_get_profile_matrix():
    profile_matrix = problem.get_profile_matrix(sequences)
    expected_a = [5, 1, 0, 0, 5, 5, 0, 0]
    expected_c = [0, 0, 1, 4, 2, 0, 6, 1]
    expected_g = [1, 1, 6, 3, 0, 1, 0, 0]
    expected_t = [1, 5, 0, 0, 0, 1, 1, 6]
    assert profile_matrix.A == expected_a
    assert profile_matrix.C == expected_c
    assert profile_matrix.G == expected_g
    assert profile_matrix.T == expected_t


def test_get_consensus_string():
    matrix = problem.get_profile_matrix(sequences)
    result = problem.get_consensus_string(matrix)
    expected_string = 'ATGCAACT'
    assert result == expected_string
