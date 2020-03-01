from rps.heredity_problems.mendels_first_law import probability_of_dominants
from pytest import approx


def test_probability_of_dominants():
    values = ["2 2 2"]
    expected_probability = 0.78333
    probability = float(probability_of_dominants(values))
    assert probability == approx(expected_probability, abs=1e-4)
