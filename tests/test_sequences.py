import pytest as pt
import rps.sequences as seq


def test_sequence_creation():
    """
    Checks if the class instance is created properly
    """
    strand = seq.NucleotideSequence('ATGC', 'MyTag')
    assert strand.sequence == 'ATGC'
    assert strand.tag == "MyTag"


def test_count_dna_nucleotides():
    """
    Checks if the function properly counts the DNA nucleotides and outputs ACGT tuple
    """
    import rps.sequence_problems.counting_DNA_nucleotides as cdn
    sequence = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    output = (20, 12, 17, 21)
    assert cdn.count_nucleotides(sequence) == output


def test_transcribing_dna_into_rna():
    """
    Checks if transcription properly replaces T with U
    """
    import rps.sequence_problems.transcribing_DNA_into_RNA as dtr
    sequence = "GATGGAACTTGACTACGTAAATT"
    output = "GAUGGAACUUGACUACGUAAAUU"
    assert dtr.transcribe(sequence) == output


def test_complementing_a_strand_of_dna():
    """
    Checks if the function returns proper reverse complement
    """
    import rps.sequence_problems.complementing_a_strand_of_DNA as csd
    sequence = "AAAACCCGGT"
    output = "ACCGGGTTTT"
    assert csd.complement_dna(sequence) == output


def test_dna_reverse_complement():
    dna = seq.DNA('ATGC', 'MyTag')
    assert dna.reverse_complement().sequence == 'GCAT'


def test_finding_motif_in_dna():
    sequence = 'GATATATGCATATACTT'
    motif = 'ATAT'
    positions = seq.search_for_motif(sequence, motif)
    assert positions == [2, 4, 10]


def test_calculate_hamming_distance():
    sample1 = 'GAGCCTACTAACGGGAT'
    sample2 = 'CATCGTAATGACGGCCT'
    seq1 = seq.DNA(sample1)
    seq2 = seq.DNA(sample2)
    hamming_distance = seq.calculate_hamming_distance(seq1, seq2)
    assert hamming_distance == 7


def test_translate_to_protein():
    sample_sequence = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    rna_strand = seq.RNA(sample_sequence)
    protein = rna_strand.translate_to_protein()
    assert protein.sequence == 'MAMAPRTEINSTRING'


def test_calculate_protein_mass():
    sample_sequence = 'SKADYEK'
    expected_mass = 821.392
    protein = seq.Peptide(sample_sequence)
    mass = protein.calculate_mass()
    assert mass == pt.approx(expected_mass)
