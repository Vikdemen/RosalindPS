"""Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of
corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not
exceeding 1 kbp). Return: The Hamming distance dH(s,t).
"""
import rps.sequences as seq
import rps.io_manager as io


def main():
    seq1, seq2 = io.read_file('input.txt')
    hamming_distance = seq.calculate_hamming_distance(seq1, seq2)
    print(hamming_distance)


if __name__ == '__main__':
    main()
