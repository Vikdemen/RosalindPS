import rps.sequences as seq
import rps.io_manager as io


def main():
    seq1, seq2 = io.read_file('input.txt')
    dna1 = seq.DNA(seq1)
    dna2 = seq.DNA(seq2)
    hamming_distance = seq.calculate_hamming_distance(dna1, dna2)
    print(hamming_distance)


if __name__ == '__main__':
    main()

