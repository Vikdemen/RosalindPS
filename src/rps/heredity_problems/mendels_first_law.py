"""
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals
are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant
allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""

from __future__ import annotations

from rps.heredity_problems.mendel import Locus, calculate_dominant_probabilities


def main():
    genotype_counts = {Locus.dom: int(input("Number of dominants (k) is ")),
                       Locus.het: int(input("Number of heterozygous (m) is ")),
                       Locus.rec: int(input("Number of recessive(n) is "))}
    dominant = calculate_dominant_probabilities(genotype_counts)
    print(round(dominant, 5))


if __name__ == '__main__':
    main()
