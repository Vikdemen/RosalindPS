"""
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals
are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant
allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""

from __future__ import annotations
from typing import Dict, Tuple
from itertools import combinations_with_replacement
from enum import Enum


class Locus(Enum):
    dom = 2
    het = 1
    rec = 0

    @staticmethod
    def gamete_chance(locus: Locus, dominant: bool = True) -> float:
        chance = locus.value/2 if dominant else abs(locus.value/2 - 1)
        return chance

    @staticmethod
    def mate(father: Locus, mother: Locus) -> Dict[Locus, float]:
        """
        :param father: alleles of a father
        :param mother: alleles of a mother
        :return: dictionary with probabilities of each genotype
        """
        domprob = offspring_chance(father, mother, Locus.dom)
        hetprob = offspring_chance(father, mother, Locus.het)
        recprob = offspring_chance(mother, mother, Locus.rec)
        genotype_probabilities = {Locus.rec: recprob, Locus.het: hetprob, Locus.dom: domprob}
        return genotype_probabilities


def offspring_chance(father: Locus, mother: Locus, child: Locus) -> float:
    father_chance = Locus.gamete_chance(father)
    mother_chance = Locus.gamete_chance(mother)
    if child == Locus.dom:
        chance = father_chance * mother_chance
    # chance of occurence of only one independent event
    elif child == Locus.het:
        chance = father_chance + mother_chance - 2 * father_chance * mother_chance
    # child == Locus.rec
    else:
        chance = (1 - father_chance) * (1 - mother_chance)
    return chance


def main():
    genotype_counts = {}
    genotype_counts[Locus.dom] = 2
    genotype_counts[Locus.het] = 2
    genotype_counts[Locus.rec] = 2
    dominant = calculate_dominant_probabilities(genotype_counts)
    print(round(dominant, 5))


def calculate_dominant_probabilities(counts: Dict[Locus, int]) -> float:
    """
    :param counts: how many creaturs of each genotype is in the pool
    :return: Total probability to get offspring with dominant allele after random mating
    """
    mating_probabilities = mating_combinations(counts).items()
    probability_sum = 0
    for pair, prob in mating_probabilities:
        gen1, gen2 = pair
        variants: Dict[Locus, float] = Locus.mate(gen1, gen2)
        probability_sum += (variants[Locus.het] + variants[Locus.dom]) * prob
    # it.s probability
    assert 0 <= probability_sum <= 0
    return probability_sum


def mating_combinations(counts: Dict[Locus, int]) -> Dict[Tuple[Locus, Locus], float]:
    comb = combinations_with_replacement((Locus.dom, Locus.het, Locus.rec), 2)
    probs = {genot: mating_probability(genot[0], genot[1], counts) for genot in comb}
    return probs


def mating_probability(gen_1: Locus, gen_2: Locus, counts: Dict[Locus, int]):
    if gen_1 == gen_2:
        count = counts[gen_2] - 1
    else:
        count = counts[gen_2]
        # we assume you can't mate with yourself
    probability = count / (sum(counts.values()) - 1)
    return probability


if __name__ == '__main__':
    main()

#TODO - wrong values, need more tests