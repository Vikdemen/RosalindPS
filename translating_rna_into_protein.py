import rps_sequences as seq
import rps_io_manager as file


def main():
    rna_sequence = file.read_file('input.txt')[0]
    translated = translate_dna(rna_sequence)
    print(translated)


def translate_dna(sequence: str) -> str:
    rna = seq.RNA(sequence)
    protein = rna.translate_to_protein()
    return protein.sequence


if __name__ == '__main__':
    main()
