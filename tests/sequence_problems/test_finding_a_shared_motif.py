from src.rps.sequence_problems.finding_a_shared_motif import longest_substring


def test_longest_substring():
    sample_data = [
        ">tag1",
        "GATTACA",
        ">tag2",
        "TAGACCA",
        ">tag3",
        "ATACA"
    ]
    expected_substring = "AC"
    longest = longest_substring(sample_data)
    # there may be several substrings of same length
    assert len(longest) == len(expected_substring)
