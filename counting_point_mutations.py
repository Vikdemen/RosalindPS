import rps_sequences as bio


def main():
    sequences = bio.read_files('input.txt')
    seq1 = bio.DNA(sequences[0])
    seq2 = bio.DNA(sequences[1])
    hamming_distance = bio.calculate_hamming_distance(seq1, seq2)
    print(hamming_distance)


if __name__ == '__main__':
    main()

