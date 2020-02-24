"""
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all
occurrences of 'T' in t with 'U' in u.
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""
import rps.sequence_problems.sequences as seq


def main():
    sequence = input("Enter DNA sequence \n")
    transcribed = transcribe(sequence)
    print(transcribed)


def transcribe(dna_sequence: str) -> str:
    """
    :param dna_sequence: DNA sequence to be transcribed
    :return: Transcribed non-reversed sequence with T replaced with U
    """
    dna = seq.DNA(dna_sequence)
    rna = dna.transcribe()
    return rna.sequence


if __name__ == '__main__':
    main()
