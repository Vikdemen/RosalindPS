"""
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals
are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant
allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""
from __future__ import annotations
from typing import List
from rps.heredity_problems.mendel import calculate_dominant_probabilities


def probability_of_dominants(lines: List[str]):
    """
    :param lines: A single line with 3 space-separated numbers representing number of organism with dominant homozygous,
    heterozygous and recessive homozygous
    :return: The probability of offspring with dominant allele from 2 random parents
    """
    line, = lines
    k, m, n = [int(num) for num in line.split()]
    dominant = calculate_dominant_probabilities(k, m, n)
    return f"{round(dominant, 5)}"
