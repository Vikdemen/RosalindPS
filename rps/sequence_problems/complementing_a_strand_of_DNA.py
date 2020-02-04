import rps.sequences as seq


def main():
    sequence = input("Enter the DNA sequence \n")
    reverse_complement = complement_dna(sequence)
    print(reverse_complement)


def complement_dna(dna_sequence: str) -> str:
    """
    :param dna_sequence: str, a string of ATGC
    :return: str, reversed RNA sequence
    """
    dna = seq.DNA(dna_sequence)
    reverse_complement = dna.reverse_complement()
    return reverse_complement.sequence


if __name__ == '__main__':
    main()
