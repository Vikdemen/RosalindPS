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