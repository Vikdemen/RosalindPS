"""
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters
except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic
string will incorporate protein strings along with DNA strings and RNA strings.
The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.
"""
import rps.sequences as seq
import rps.io_manager as file


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
