"""
Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
Above, we use 1-based numbering, as opposed to 0-based numbering, which is used in Python.
"""
import rps.sequences as seq


def main():
    """
    Prints all 1-based positions of substring (2d input) in a string(1st input)
    """
    sequence = input("Input the sequence")
    motif = input("Input the motif")
    positions = seq.search_for_motif(sequence, motif)
    print(*positions)


if __name__ == '__main__':
    main()
