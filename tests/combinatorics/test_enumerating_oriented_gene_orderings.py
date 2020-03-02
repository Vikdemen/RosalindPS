from rps.combinatorics.enumerating_oriented_gene_orderings import get_signed_permutations


def test_get_signed_permutations():
    sample_value = ['2']
    expected_number = 8
    expected_permutations = {
        "-1 -2",
        "-1 2",
        "1 -2",
        "1 2",
        "-2 -1",
        "-2 1",
        "2 -1",
        "2 1"
    }
    result = get_signed_permutations(sample_value).split('\n')
    number = int(result[0])
    signed_permutations = set(result[1:])
    assert number == expected_number
    assert signed_permutations == expected_permutations
