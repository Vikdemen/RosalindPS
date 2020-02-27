from rps.sequence_problems.rna_splicing import splice_and_translate


def test_splice_and_translate():
    sample_data = [
        "> Rosalind_10",
        "ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG",
        "> Rosalind_12",
        "ATCGGTCGAA",
        "> Rosalind_15",
        "ATCGGTCGAGCGTGT"
    ]
    expected_protein = "MVYIADKQHVASREAYGHMFKVCA"
    # noinspection PyTypeChecker
    protein = splice_and_translate(sample_data)
    assert protein == expected_protein
