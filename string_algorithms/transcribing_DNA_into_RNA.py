import rps_sequences


def main():
    sequence = input("Enter DNA sequence \n")
    transcribed = transcribe(sequence)
    print(transcribed)


def transcribe(dna_sequence: str) -> str:
    """
    :param dna_sequence: DNA sequence to be transcribed
    :return: Transcribed non-reversed sequence with T replaced with U
    """
    dna = rps_sequences.DNA(dna_sequence)
    rna = dna.transcribe()
    return rna.sequence


if __name__ == '__main__':
    main()
