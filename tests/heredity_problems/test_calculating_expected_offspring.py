from pytest import approx

from rps.heredity_problems.calculating_expected_offspring import expected_dominant_offspring


def test_expected_dominant_offspring():
    values = ["1 0 0 1 0 1"]
    expected_offspring = 3.5
    offspring = float(expected_dominant_offspring(values))
    assert offspring == approx(expected_offspring)

