from rps.combinatorics.enumerating_kmers_lexicographically import enumerate_kmers


def test_enumerate_kmers():
    """
    Sample data for problem "Enumerating k-mers Lexicographically"
    :return:
    """
    alphabet = "A C G T"
    n = 2
    expected_result = \
        """AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT"""
    result = enumerate_kmers([alphabet, str(n)])
    assert result == expected_result
