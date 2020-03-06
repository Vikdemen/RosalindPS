"""
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4)
is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
"""
from typing import Sequence
from itertools import permutations


def get_permutations(lines: Sequence[str]) -> str:
    """
    :param lines:  A line with n, a positive integer
    :return: Number of permutations followed by permutations of numbers between 1 and n
    """
    if len(lines) != 1:
        raise ValueError("There must be only 1 line of input")
    line, *_ = lines[0]
    n = int(line)
    if n <= 0:
        raise ValueError("N must be a positive integer")
    # casting to list to get the total number
    permutations_ = list(permutations(range(1, n+1)))
    formatted_permutations = '\n'.join([' '.join((str(number) for number in nums)) for nums in permutations_])
    return f"{len(permutations_)}\n{formatted_permutations}"
