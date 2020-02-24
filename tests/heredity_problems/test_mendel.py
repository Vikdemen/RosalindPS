import rps.heredity_problems.mendel
import pytest as pt


@pt.mark.parametrize('locus, dominant, expected', [(rps.heredity_problems.mendel.Locus.dom, True, 1), (
        rps.heredity_problems.mendel.Locus.dom, False, 0),
                                                   (rps.heredity_problems.mendel.Locus.het, True, 0.5), (
                                                           rps.heredity_problems.mendel.Locus.het, False, 0.5),
                                                   (rps.heredity_problems.mendel.Locus.rec, True, 0), (
                                                           rps.heredity_problems.mendel.Locus.rec, False, 1)])
def test_gamete_chance(locus: rps.heredity_problems.mendel.Locus, dominant: bool, expected: float) -> None:
    assert rps.heredity_problems.mendel.Locus.gamete_chance(locus, dominant) == pt.approx(expected)


@pt.mark.parametrize('father, mother, child, probability', [(rps.heredity_problems.mendel.Locus.dom, rps.heredity_problems.mendel.Locus.dom, rps.heredity_problems.mendel.Locus.dom, 1),
                                                            (rps.heredity_problems.mendel.Locus.dom, rps.heredity_problems.mendel.Locus.rec, rps.heredity_problems.mendel.Locus.het, 1),
                                                            (rps.heredity_problems.mendel.Locus.dom, rps.heredity_problems.mendel.Locus.rec, rps.heredity_problems.mendel.Locus.rec, 0),
                                                            (rps.heredity_problems.mendel.Locus.dom, rps.heredity_problems.mendel.Locus.dom, rps.heredity_problems.mendel.Locus.rec, 0)])
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