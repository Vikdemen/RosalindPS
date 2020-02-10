import rps.heredity.mendels_first_law as md
import pytest as pt


@pt.mark.parametrize('locus, dominant, expected', [(md.Locus.dom, True, 1), (md.Locus.dom, False, 0),
                                                   (md.Locus.het, True, 0.5), (md.Locus.het, False, 0.5),
                                                   (md.Locus.rec, True, 0), (md.Locus.rec, False, 1)])
def test_gamete_chance(locus: md.Locus, dominant: bool, expected: float) -> None:
    assert md.Locus.gamete_chance(locus, dominant) == pt.approx(expected)


@pt.mark.parametrize('father, mother, child, probability', [(md.Locus.dom, md.Locus.dom, md.Locus.dom, 1),
                                                            (md.Locus.dom, md.Locus.rec, md.Locus.het, 1),
                                                            (md.Locus.dom, md.Locus.rec, md.Locus.rec, 0),
                                                            (md.Locus.dom, md.Locus.dom, md.Locus.rec, 0)])
def test_offspring_chance(father, mother, child, probability):
    assert md.offspring_chance(father, mother, child) == pt.approx(probability)
