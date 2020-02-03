from collections import Counter
from typing import Dict


# class Sequence:
# def __init__(self, sequence):
# self.sequence = sequence


class NucleotideSequence:
    def __init__(self, sequence: str, tag="N/A"):
        """
        :param sequence: str A sequence of nucleotides
        :param tag: str Fasta tag, defaults to N/A
        """
        self.sequence = sequence
        self.tag = tag

    def count_bases(self) -> Dict[str, int]:
        """
        :return: a dictionary of nucleotides and their respective counts
        """
        counts = Counter(self.sequence)
        return counts


class DNA(NucleotideSequence):
    type = "DNA"

    COMPLEMENTARY_BASES = {"A": "T", "T": "A", "G": "C", "C": "G"}

    def transcribe(self):
        new_sequence = self.sequence.replace('T', 'U')
        return RNA(new_sequence)

    def reverse_complement(self):
        new_sequence = ""
        for base in self.sequence[::-1]:
            new_sequence += DNA.COMPLEMENTARY_BASES[base]
        return DNA(new_sequence)

    def gc_content(self):
        bases = self.count_bases()
        c = bases[1]
        g = bases[2]
        gc = (g + c) / sum(bases) * 100
        return gc


class Peptide:
    def __init__(self, sequence: str):
        self.sequence = sequence


class RNA(NucleotideSequence):
    type = "RNA"

    def translate_to_protein(self) -> Peptide:
        peptide_seq = []
        codons = [self.sequence[i:i+3] for i in range(len(self.sequence))[::3]]
        for codon in codons:
            amino = GENETIC_CODE[codon]
            if amino == 'X':
                # stop codon
                break
            else:
                peptide_seq.append(amino)
        return Peptide(''.join(peptide_seq))


def calculate_hamming_distance(seq1: NucleotideSequence, seq2: NucleotideSequence) -> int:
    pairs = zip(seq1.sequence, seq2.sequence)
    return len([pair for pair in pairs if pair[0] != pair[1]])


# Calculates the number of mismatched bases between two sequences
# We assume that sequences are of equal length


GENETIC_CODE = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': 'X', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': 'X', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': 'X', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}
# X is stop-codon
