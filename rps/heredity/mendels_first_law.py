from typing import Dict, Tuple
from itertools import combinations_with_replacement as cwr
from itertools import product

DOM = 2
HET = 1
REC = 0

class Genotype:
    def __init__(self, gene: Tuple[int, int]):
        self.gene = gene

    def mate(self, other):
        mate1 = self.gene
        mate2 = other.gene
        entries = {REC: 0, HET: 0, DOM: 0}
        matrix = product(mate1, mate2)
        matrix = map(get_alleles, matrix)
        #TODO - unfinished
        return entries

def get_alleles(gene):
    alleles = {True : 0.0, False: 0.0}
    if gene == HET:
        alleles[True] = 0.5
        alleles[False] = 0.5
    if gene == DOM:
        alleles[True] = 1

    return alleles

class Probabilities:
    def __init__(self):
        self.values = {0: 0, 1: 0, 2: 0}

    def mult(self, multiplier):
        for key, val in self.values.items():
            self.values[key] = val * multiplier


genotype_counts = {REC: 2, HET: 2, DOM: 2}


def mating_combinations():
    comb = cwr((REC, HET, DOM), 2)
    probs = {genot: mating_probability(*genot) for genot in comb}
    return probs


def mating_probability(gen_1, gen_2):
    genotype_counts[gen_1] -= 1
    probability = genotype_counts[gen_2] / sum(genotype_counts.values())
    return probability

def dominant_probability(gen1, gen2):
    gen1 = Genotype(gen1)
    gen2 = Genotype(gen2)
    offspring = gen1.mate(gen2)
    result = sum(prob for genot, prob in offspring.items() if genot == DOM or HET)


mating_probabilities = ((gen, prob) for gen, prob in mating_combinations().items())
dominant = sum((dominant_probability(*gen) * mate_prob for gen, mate_prob in mating_probabilities))
print(round(dominant), 5)
