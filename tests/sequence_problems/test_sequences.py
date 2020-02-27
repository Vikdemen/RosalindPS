import src.rps.sequence_problems.sequences as seq


def test_sequence_creation():
    """
    Checks if the class instance is created properly
    """
    strand = seq.NucleotideSequence('ATGC', 'MyTag')
    assert strand.sequence == 'ATGC'
    assert strand.tag == "MyTag"


def test_dna_reverse_complement():
    dna = seq.DNA('ATGC', 'MyTag')
    assert dna.reverse_complement().sequence == 'GCAT'




