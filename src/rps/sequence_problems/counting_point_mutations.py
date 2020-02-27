"""Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of
corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not
exceeding 1 kbp). Return: The Hamming distance dH(s,t).
"""
import rps.sequence_problems.sequences as seq
import rps.io_manager as io


def main():
    seq1, seq2 = io.read_file('input.txt')
    hamming_distance = get_hamming_distance(seq1, seq2)
    print(hamming_distance)


def get_hamming_distance(seq1, seq2):
    strand1 = seq.DNA(seq1)
    strand2 = seq.DNA(seq2)
    distance = strand1.calculate_hamming_distance(strand2)
    return distance


if __name__ == '__main__':
    main()
