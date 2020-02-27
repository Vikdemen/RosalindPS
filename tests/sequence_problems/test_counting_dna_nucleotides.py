from rps.sequence_problems.counting_dna_nucleotides import count_nucleotides


def test_count_dna_nucleotides():
    """
    Checks if the function properly counts the DNA nucleotides and outputs ACGT tuple
    """
    sequence = ['AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC']
    output = (20, 12, 17, 21)
    assert count_nucleotides(sequence) == output
