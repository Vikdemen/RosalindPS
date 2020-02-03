import pytest
import rps_sequences as bio


def test_dna_creation():
    """
    Checks if the class instance is created properly
    """
    seq = bio.NucleotideSequence('ATGC', 'MyTag')
    assert seq.sequence == 'ATGC'
    assert seq.tag == "MyTag"


def test_count_dna_nucleotides():
    """
    Checks if the function properly counts the DNA nucleotides and outputs ACGT tuple
    """
    import string_algorithms.counting_DNA_nucleotides as cdn
    sequence = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    output = (20, 12, 17, 21)
    assert cdn.count_nucleotides(sequence) == output


def test_transcribing_dna_into_rna():
    """
    Checks if transcription properly replaces T with U
    """
    import string_algorithms.transcribing_DNA_into_RNA as dtr
    sequence = "GATGGAACTTGACTACGTAAATT"
    output = "GAUGGAACUUGACUACGUAAAUU"
    assert dtr.transcribe(sequence) == output


def test_complementing_a_strand_of_dna():
    """
    Checks if the function returns proper reverse complement
    """
    import string_algorithms.complementing_a_strand_of_DNA as csd
    sequence = "AAAACCCGGT"
    output = "ACCGGGTTTT"
    assert csd.complement_dna(sequence) == output


def test_dna_reverse_complement():
    seq = bio.DNA('ATGC', 'MyTag')
    assert seq.reverse_complement().sequence == 'GCAT'


def test_calculate_hamming_distance():
    sample1 = 'GAGCCTACTAACGGGAT'
    sample2 = 'CATCGTAATGACGGCCT'
    seq1 = bio.DNA(sample1)
    seq2 = bio.DNA(sample2)
    hamming_distance = bio.calculate_hamming_distance(seq1, seq2)
    assert hamming_distance == 7


def test_translate_to_protein():
    sample_sequence = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    rna_strand = bio.RNA(sample_sequence)
    protein = rna_strand.translate_to_protein()
    assert protein.sequence == 'MAMAPRTEINSTRING'
