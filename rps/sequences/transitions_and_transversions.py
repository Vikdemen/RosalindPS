import rps_io_manager as file
import rps_sequences as seq


def calculate_tt_ratio(fasta_sequences):
    tagged_sequences = file.parse_fasta(fasta_sequences)
    first, second = [seq.DNA(sequence, tag) for sequence, tag in tagged_sequences]
    transitions, transversions = first.transitions_transversions(second)
    tt_ratio = transitions/transversions
    return tt_ratio


def main():
    fasta_sequences = file.read_file("input.txt")
    ratio = calculate_tt_ratio(fasta_sequences)
    print(round(ratio, 11))


if __name__ == '__main__':
    main()