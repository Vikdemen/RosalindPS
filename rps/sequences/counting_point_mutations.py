import rps.sequences as seq


def main():
    sequences = seq.read_files('input.txt')
    seq1 = seq.DNA(sequences[0])
    seq2 = seq.DNA(sequences[1])
    hamming_distance = seq.calculate_hamming_distance(seq1, seq2)
    print(hamming_distance)


if __name__ == '__main__':
    main()

