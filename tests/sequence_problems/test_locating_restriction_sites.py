from rps.sequence_problems.locating_restriction_sites import palindrome_positions


def test_palindrome_positions():
    sample_dataset = [
        ">Rosalind_24",
        "TCAATGCATGCGGGTCTATATGCAT"
    ]
    pairs = set(palindrome_positions(sample_dataset).split('\n'))
    expected_pairs = {
        "4 6",
        "5 4",
        "6 6",
        "7 4",
        "17 4",
        "18 4",
        "20 6",
        "21 4"
    }
    assert pairs == expected_pairs
