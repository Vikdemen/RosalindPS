import rps.sequences as seq


def main():
    """
    :return: Prints all 1-based positions of substring (2d input) in a string(1st input)
    """
    sequence = input("Input the sequence")
    motif = input("Input the motif")
    positions = seq.search_for_motif(sequence, motif)
    print(*positions)


if __name__ == '__main__':
    main()
