"""
Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
Above, we use 1-based numbering, as opposed to 0-based numbering, which is used in Python.
"""
import rps.sequence_problems.sequences as seq


def main():
    """
    Prints all 1-based positions of substring (2d input) in a string(1st input)
    """
    sequence = input("Input the sequence")
    motif = input("Input the motif")
    positions = get_motif_positions(sequence, motif)
    print(*positions)


def get_motif_positions(sequence, motif):
    strand = seq.DNA(sequence)
    return strand.search_for_motif(motif)


if __name__ == '__main__':
    main()
