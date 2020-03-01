"""
Rabbits die out after a fixed number of months.
Given: Positive integers n≤100 and m≤20.
Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""
from typing import List
import rps.dynamic_programming_problems.fibonacci as fib


def count_mortal_rabbits(lines: List[str]):
    """
    :param lines: Line with time in month and lifespan of rabbits, separated by space
    :return: Total number of rabbit pairs after that time
    """
    line, = lines
    time, lifespan = map(int, line.split())
    rabbits = fib.count_mortal_rabbits(time, lifespan)
    return rabbits
