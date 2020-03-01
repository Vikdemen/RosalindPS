import rps.sequence_problems.sequences as seq


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


def test__is_reverse_palindrome():
    assert seq.DNA('GCATGC').is_reverse_palindrome
    assert not seq.DNA('GCACGT').is_reverse_palindrome


def test_find_reverse_palindromes():
    dna = seq.DNA('CCCCGCATGCAAAA')
    palindromes = dna.find_reverse_palindromes(6, 8)
    assert palindromes == [(5, 6)]
