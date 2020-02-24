from rps.sequence_problems.transitions_and_transversions import calculate_tt_ratio
from pytest import approx


def test_calculate_tt_ratio():
    sample_sequences = [
        ">Rosalind_0209",
        "GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA",
        "AGTACGGGCATCAACCCAGTT",
        ">Rosalind_2200",
        "TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC",
        "GGTACGAGTGTTCCTTTGGGT"
    ]
    ratio = calculate_tt_ratio(sample_sequences)
    expected_ratio = 1.21428571429
    assert ratio == approx(expected_ratio)
