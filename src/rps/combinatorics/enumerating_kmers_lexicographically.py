"""
Assume that an alphabet A has a predetermined order; that is, we write the alphabet as a permutation A=(a1,a2,…,
ak), where a1<a2<⋯<ak. For instance, the English alphabet is organized as (A,B,…,Z).

Given two strings s and t having the same length n, we say that s precedes t in the lexicographic order
(and write s<t) if the first symbol s[j] that doesn't match t[j] satisfies sj<tj in A.

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard
order of symbols in the English alphabet). """

from typing import List, Iterable, Sequence
from itertools import product


def enumerate_kmers(lines: Sequence[str]) -> str:
    alphabet, n = lines
    alphabet = alphabet.split()
    n = int(n)
    if n <= 0:
        raise ValueError("N must be a positive integer")
    ordered_strings = get_ordered_kmers(alphabet, n)
    return '\n'.join(ordered_strings)


def get_ordered_kmers(alphabet: Iterable[str], length: int) -> List[str]:
    # all formable strings is cartesian product
    products = product(alphabet, repeat=length)
    # they are emitted as tuples
    possible_strings = [''.join(letters) for letters in products]
    ordered_strings = sorted(possible_strings)
    return ordered_strings
