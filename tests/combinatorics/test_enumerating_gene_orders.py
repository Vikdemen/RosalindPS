from rps.combinatorics.enumerating_gene_orders import get_permutations


def test_get_permutations():
    sample_value = ['3']
    expected_number = 6
    expected_permutations = {
        "1 2 3",
        "1 3 2",
        "2 1 3",
        "2 3 1",
        "3 1 2",
        "3 2 1"
    }
    result = get_permutations(sample_value).split('\n')
    number = int(result[0])
    permutations = set(result[1:])
    assert number == expected_number
    assert permutations == expected_permutations
