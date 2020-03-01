"""
Given: Positive integers n≤40 and k≤5.
Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each
generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
"""
from typing import List

import rps.dynamic_programming_problems.fibonacci as fib


def count_rabbits(lines: List[str]) -> int:
    """
    :param lines: A line with the time in month and number of offsping pairs in litter, separated by space
    :return: Total number of rabbit pairsafter that time
    """
    line, = lines
    time, litter = map(int, line.split())
    rabbits = fib.count_rabbits(time, litter)
    return rabbits
