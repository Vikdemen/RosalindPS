from rps.sequence_problems.translating_rna_into_protein import translate_dna


def test_translate_dna():
    """
    Checks if DNA sequence translates into correct protein
    :return:
    """
    sample_sequence = ['AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA']
    expected_protein = 'MAMAPRTEINSTRING'
    # noinspection PyTypeChecker
    protein_sequence = translate_dna(sample_sequence)
    assert protein_sequence == expected_protein
