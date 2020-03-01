"""
Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence
relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair
of offspring (one male, one female) each subsequent month.
Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all
rabbits die out after a fixed number of months. For example, if rabbits live for three months, they reproduce only
twice before dying.

Given: Positive integers n≤100 and m≤20.
Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""
from typing import List
import rps.dynamic_programming_problems.fibonacci as fib


def count_mortal_rabbits(lines: List[str]) -> str:
    """
    :param lines: Line with time in month and lifespan of rabbits, separated by space
    :return: Total number of rabbit pairs after that time
    """
    line, = lines
    time, lifespan = map(int, line.split())
    rabbits = fib.count_mortal_rabbits(time, lifespan)
    return f"{rabbits}"
