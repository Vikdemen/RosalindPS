import rps.sequences as seq
import rps.io_manager as io


def main():
    """
    Problem
    In a weighted alphabet, every symbol is assigned a positive real number called a weight. A string formed from
    a weighted alphabet is called a weighted string, and its weight is equal to the sum of the weights of its symbols.
    The standard weight assigned to each member of the 20-symbol amino acid alphabet is the monoisotopic mass of
    the corresponding amino acid.
    Given: A protein string P of length at most 1000 aa.
    Return: The total weight of P. Consult the monoisotopic mass table.
    """
    # unpacking a single line from list
    sequence, = io.read_file("input.txt")
    mass = calculate_mass(sequence)
    print(round(mass), 4)


def calculate_mass(sequence: str) -> float:
    """
    :param sequence: a sequence of aminoacids in the form of the string using 1-letter notation
    :return: Monoisotopic mass of peptide chain with a given sequence of residues
    """
    peptide = seq.Peptide(sequence)
    mass = peptide.calculate_mass()
    return mass


if __name__ == '__main__':
    main()
