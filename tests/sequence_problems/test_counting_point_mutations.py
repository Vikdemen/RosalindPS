from rps.sequence_problems.counting_point_mutations import get_hamming_distance


def test_calculate_hamming_distance():
    sample1 = 'GAGCCTACTAACGGGAT'
    sample2 = 'CATCGTAATGACGGCCT'
    hamming_distance = int(get_hamming_distance([sample1, sample2]))
    expected_distance = 7
    assert hamming_distance == expected_distance
