"""
A signed permutation of length n is some ordering of the positive integers {1,2,…,n} in which each integer is then
provided with either a positive or negative sign (for the sake of simplicity, we omit the positive sign). For
example, π=(5,−3,−2,1,4) is a signed permutation of length 5.
Given: A positive integer n≤6.
Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may
list the signed permutations in any order).
"""
from itertools import permutations, chain, product
from typing import List


def get_signed_permutations(lines: List[str]) -> str:
    line, = lines
    n = int(line)
    if n <= 0:
        raise ValueError("N must be a positive integer")
    # getting permutations
    unsigned_permutations = permutations(range(1, n + 1))
    # we turn each permutation into several variants with different signs
    signed_permutations = (_signed_from_unsigned(unsigned) for unsigned in unsigned_permutations)
    # combining the variants into a single list
    signed_permutations = list(chain.from_iterable(signed_permutations))
    # make each variant a space separated string
    formatted_permutations = [' '.join((str(num) for num in _permutation)) for _permutation in signed_permutations]
    signed_permutations_number = len(formatted_permutations)
    formatted_permutations = '\n'.join(formatted_permutations)
    return f"{signed_permutations_number}\n{formatted_permutations}"


def _signed_from_unsigned(_permutation):
    # for each number, we have 2 variants
    sign_variants = ((digit, -digit) for digit in _permutation)
    # then we combine them in all possible ways
    all_variants = product(*sign_variants)
    return all_variants
