from rps.sequence_problems.complementing_a_strand_of_dna import complement_dna


def test_complement_dna():
    """
    Checks if the function returns proper reverse complement
    """
    sequence = ["AAAACCCGGT"]
    expected_complement = "ACCGGGTTTT"
    complement = complement_dna(sequence)
    assert complement == expected_complement
