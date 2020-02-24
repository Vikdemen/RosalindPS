import rps.heredity_problems.mendel
from rps.heredity_problems.mendel import Locus
import pytest as pt


@pt.mark.parametrize('locus, dominant, expected', [
    (Locus.dom, True, 1),
    (Locus.dom, False, 0),
    (Locus.het, True, 0.5),
    (Locus.het, False, 0.5),
    (Locus.rec, True, 0),
    (Locus.rec, False, 1)])
def test_gamete_chance(locus: rps.heredity_problems.mendel.Locus, dominant: bool, expected: float) -> None:
    assert rps.heredity_problems.mendel.Locus.gamete_chance(locus, dominant) == pt.approx(expected)


@pt.mark.parametrize('father, mother, child, probability', [
    (Locus.dom, Locus.dom, Locus.dom, 1),
    (Locus.dom, Locus.rec, Locus.het, 1),
    (Locus.dom, Locus.rec, Locus.rec, 0),
    (Locus.dom, Locus.dom, Locus.rec, 0)])
def test_offspring_chance(father, mother, child, probability):
    assert rps.heredity_problems.mendel.offspring_chance(father, mother, child) == pt.approx(probability)

# def test_mating_combinations():
#     counts = {md.Locus.dom: 2, md.Locus.het: 2, md.Locus.rec: 2}
#     total = sum(counts.values())
#     combinations = md.mating_combinations(counts)
#     assert len(combinations.items()) == 9
#     for pair, probability in combinations.items():
#         father, mother = pair
#         if father == mother:
#             assert probability == counts[father] / total * (counts[father] - 1) / (total - 1)
#         else:
#             assert probability == counts[father] / total * counts[mother] / total
