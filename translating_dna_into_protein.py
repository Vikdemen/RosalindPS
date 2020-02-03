import rps_sequences as bio
import rps_io_manager as file


def main():
    rna_sequence = file.read_file('input.txt')[0]
    rna = bio.RNA(rna_sequence)
    protein = rna.translate_to_protein()
    print(protein.sequence)


if __name__ == '__main__':
    main()
