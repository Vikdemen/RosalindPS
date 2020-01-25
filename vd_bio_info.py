from typing import List


# class Sequence:
# def __init__(self, sequence):
# self.sequence = sequence


class NucleotideSequence:
    def __init__(self, new_sequence, new_tag="unnamed"):
        self.sequence = new_sequence
        self.tag = new_tag


class DNA(NucleotideSequence):
    type = "DNA"

    complements = {"A": "T", "T": "A", "G": "C", "C": "G"}

    def count_bases(self):
        a = 0
        t = 0
        g = 0
        c = 0
        for base in self.sequence:
            if base == 'A':
                a += 1
            if base == 'T':
                t += 1
            if base == 'G':
                g += 1
            if base == 'C':
                c += 1
        return a, c, g, t

    def transcribe(self):
        new_sequence = self.sequence.replace('T', 'U')
        return RNA(new_sequence)

    def reverse_complement(self):
        new_sequence = ""
        for base in self.sequence[::-1]:
            new_sequence += DNA.complements[base]
        return DNA(new_sequence)

    def gc_content(self):
        bases = self.count_bases()
        c = bases[1]
        g = bases[2]
        gc = (g + c) / sum(bases) * 100
        return gc


class RNA(NucleotideSequence):
    type = "RNA"


# class Peptide:

def read_files(filename: str):
    with open(filename, 'r') as file:
        data = file.readlines()
    data = [line.replace('/n', '') for line in data]
    return data


def parse_fasta(data: List[str]):
    sequences = []
    i = -1
    for line in data:
        if line.startswith('>'):
            sequences.append([line[1:], ""])
            i += 1
        else:
            sequences[i][1] += line

    # throws error if the first line doesn't start with tag

    sequences = [DNA(s[1], s[0]) for s in sequences]
    return sequences
