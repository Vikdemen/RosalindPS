import pytest
import vd_bio_info as bio


def test_dna_creation():
    seq = bio.DNA('ATGC', 'MyTag')
    assert seq.sequence == 'ATGC'
    assert seq.tag == "MyTag"


def test_dna_reverse_complement():
    seq = bio.DNA('ATGC', 'MyTag')
    assert seq.reverse_complement().sequence == 'GCAT'
