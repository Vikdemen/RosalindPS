from __future__ import annotations
from collections import Counter
from itertools import takewhile
from typing import Dict, Tuple, List
from more_itertools import ichunked, windowed


class NucleotideSequence:

    valid_nucleotides = {'A', 'T', 'U', 'G', 'C'}

    def __init__(self, sequence: str, tag="N/A"):
        """
        :param sequence:A sequence of nucleotides
        :param tag:Fasta tag, defaults to N/A
        """
        if any(char not in self.valid_nucleotides for char in sequence):
            raise ValueError("Unexpected nucleotide encountered")
        self.sequence = sequence
        self.tag = tag

    def count_bases(self) -> Dict[str, int]:
        """
        :return: a dictionary of nucleotides and their respective counts
        """
        counts = Counter(self.sequence)
        return counts

    def calculate_hamming_distance(self, another: NucleotideSequence) -> int:
        """
        :param another: Another sequence of same length
        :return: Number of mismatched nucleotides between two sequences
        """
        if len(self.sequence) != len(another.sequence):
            raise ValueError("Sequences are of different length")
        pairs = zip(self.sequence, another.sequence)
        return len([pair for pair in pairs if pair[0] != pair[1]])


class DNA(NucleotideSequence):
    COMPLEMENTARY_BASES = {"A": "T", "T": "A", "G": "C", "C": "G"}
    purines = {'A', 'G'}
    pyrimidines = {'C', 'T'}
    valid_nucleotides = {'A', 'T', 'G', 'C'}

    def transitions_transversions(self, other) -> Tuple[int, int]:
        if len(self.sequence) != len(other.sequence):
            raise ValueError("Sequences must be of equal length")
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
        return RNA(new_sequence, self.tag)

    def reverse_complement(self) -> DNA:
        """
        :return: A DNA strand with complementary sequence and opposite direction
        """
        new_sequence = [DNA.COMPLEMENTARY_BASES[base] for base in self.sequence[::-1]]
        new_sequence = ''.join(new_sequence)
        return DNA(new_sequence)

    def gc_content(self) -> float:
        bases: Dict[str, int] = self.count_bases()
        c = bases['C']
        g = bases['G']
        total = sum(bases.values())
        gc = (g + c) / total * 100
        return gc

    def search_for_motif(self, motif: str, base: int = 1) -> List[int]:
        """
        :param motif: A substring to search in sequence
        :param base: 0- or 1- based numbering, 1 is default.
        :return: A list of overlapping occurences of given substring in sequence
        """
        if len(motif) > len(self.sequence):
            raise ValueError("Motif is larger than a whole sequence")
        positions = []
        start = 0
        while True:
            result = self.sequence.find(motif, start)
            if result == -1:
                break
            else:
                start = result + 1
                # uses 1-based position or 0-based index
                positions.append(result + base)
        return positions

    def search_for_orf(self) -> List[DNA]:
        def get_frames(strand: DNA, orfs: List[str]):
            start_codon_positions = strand.search_for_motif('ATG', base=0)
            for p in start_codon_positions:
                frame = strand.sequence[p:]
                assert frame.startswith('ATG')
                codons_in_frame = set(map("".join, ichunked(frame, 3)))
                # only stop-codons aligned in frame work
                if 'TAG' in codons_in_frame or 'TGA' in codons_in_frame or 'TAA' in codons_in_frame:
                    orfs.append(frame)

        open_reading_frames = []
        get_frames(self, open_reading_frames)
        get_frames(self.reverse_complement(), open_reading_frames)
        orf_strands = [DNA(seq) for seq in open_reading_frames]
        return orf_strands

    def find_reverse_palindromes(self, min_length: int, max_length: int) -> List[Tuple[int, int]]:
        """
        :param min_length: Minimum length of palindromes to search
        :param max_length: Maximum length of palindromes to search
        :return: 1-based position and length of found palindromes
        """
        if min_length < 2:
            raise ValueError("palindrome can't be shorter than 2 nucleotides")
        if max_length < min_length:
            raise ValueError("max length can't be less than minimum length")

        reverse_palindromes = []
        for length in range(min_length, max_length+1):
            windows = windowed(self.sequence, length)
            for index, window in enumerate(windows):
                if DNA(''.join(window)).is_reverse_palindrome:
                    reverse_palindromes.append((index+1, length))
        return reverse_palindromes

    @property
    def is_reverse_palindrome(self) -> bool:
        """
        :return: if the sequence is reverse palindrome
        """
        return self.sequence == self.reverse_complement().sequence


class RNA(NucleotideSequence):

    valid_nucleotides = {'A', 'U', 'G', 'C'}

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
        protein = Peptide(peptide_seq)
        return protein

    def splice(self, intron: RNA) -> RNA:
        """
        :param intron: Another RNA sequence representing intron
        :return: New RNA sequence with intron cut out
        """
        spliced = self.sequence.replace(intron.sequence, "")
        return RNA(spliced, self.tag)


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
