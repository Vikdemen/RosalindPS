from __future__ import annotations
from collections import Counter
from itertools import takewhile
from typing import Dict, Tuple, List
from more_itertools import ichunked


# class Sequence:
# def __init__(self, sequence):
# self.sequence = sequence


class NucleotideSequence:
    def __init__(self, sequence: str, tag="N/A"):
        """
        :param sequence:A sequence of nucleotides
        :param tag:Fasta tag, defaults to N/A
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
    COMPLEMENTARY_BASES = {"A": "T", "T": "A", "G": "C", "C": "G"}
    purines = {'A', 'G'}
    pyrimidines = {'C', 'T'}

    def transitions_transversions(self, other) -> Tuple[int, int]:
        transitions = 0
        transversions = 0
        for b1, b2 in zip(self.sequence, other.sequence):
            if b1 != b2:
                if b1 in DNA.purines:
                    if b2 in DNA.purines:
                        transitions += 1
                    else:
                        transversions += 1
                else:
                    if b2 in DNA.pyrimidines:
                        transitions += 1
                    else:
                        transversions += 1
        return transitions, transversions

    def transcribe(self) -> RNA:
        """
        :return: RNA strand with the same direction and thymine replaced with uracil
        """
        new_sequence = self.sequence.replace('T', 'U')
        return RNA(new_sequence)

    def reverse_complement(self) -> DNA:
        """
        :return: A DNA strand with complementary sequence and opposite direction
        """
        new_sequence = [DNA.COMPLEMENTARY_BASES[base] for base in self.sequence[::-1]]
        new_sequence = ''.join(new_sequence)
        return DNA(new_sequence)

    def gc_content(self):
        bases = self.count_bases()
        c = bases['C']
        g = bases['G']
        gc = (g + c) / sum(bases) * 100
        return gc


class Peptide:
    def __init__(self, sequence: str):
        self.sequence = sequence

    def calculate_mass(self) -> float:
        """
        :return: Mass of peptide chain
        Calculates the monoisotopic mass of protein chain, assuming it fully consists of AA residues.
        """
        mass = sum((AA_MASSES[amino] for amino in self.sequence))
        return mass


class RNA(NucleotideSequence):

    def translate_to_protein(self) -> Peptide:
        """
        :return: Returns protein chain encoded by matrix RNA, using 1-letter notation.
        Translating stops at stop-codon
        """
        # divide into 3-character strings
        codons = map("".join, ichunked(self.sequence, 3))
        # translate into aminoacids
        peptide_seq = (GENETIC_CODE[codon] for codon in codons)
        # transation stops when stop-codon is encountered
        peptide_seq = takewhile(lambda amino: amino != 'X', peptide_seq)
        # generator is joined into a string
        peptide_seq = ''.join(peptide_seq)
        return Peptide(peptide_seq)

    def splice(self, intron):
        spliced = self.sequence.replace(intron.sequence, "")
        return RNA(spliced, self.tag)


def calculate_hamming_distance(seq1: str, seq2: str) -> int:
    """
    :param seq1: string, representing nucleotide sequence
    :param seq2: Another sequence of same length
    :return: Number of mismatched nucleotides between two sequences
    """
    pairs = zip(seq1, seq2)
    return len([pair for pair in pairs if pair[0] != pair[1]])


def search_for_motif(sequence: str, motif: str) -> List[int]:
    if len(motif) > len(sequence):
        raise ValueError("Motif is larger than a whole sequence")
    positions = []
    start = 0
    while True:
        result = sequence.find(motif, start)
        if result == -1:
            break
        else:
            start = result + 1
            # we need to use 1-based numbering
            positions.append(result + 1)
    return positions


# encoding of every aminoacid by 3-base RNA sequences
# X is stop-codon
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

# monoisotopic masses of aminoacid residues
AA_MASSES = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333,
}
