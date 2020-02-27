from pytest import approx
from rps.sequence_problems.calculating_protein_mass import calculate_mass


def test_calculate_protein_mass():
    """
    Checks if it properly calculates the mass of a given protein
    :return:
    """
    sample_sequence = ['SKADYEK']
    expected_mass = 821.392
    # noinspection PyTypeChecker
    protein_mass = calculate_mass(sample_sequence)
    assert protein_mass == approx(expected_mass)
