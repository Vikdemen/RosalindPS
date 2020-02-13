"""
Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of
couples in a population possessing each genotype pairing for a given factor. In order, the six given integers
represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the
next generation, under the assumption that every couple has exactly two offspring.
"""
import rps.heredity.mendel as md


def main():
    dom = md.Locus.dom
    het = md.Locus.het
    rec = md.Locus.rec
    offspring_number = 2
    counts = list(map(int, (input("number of couples is ").split())))
    couples = {(dom, dom): counts[0], (dom, het): counts[1], (dom, rec): counts[2], (het, het): counts[3],
               (het, rec): counts[4], (rec, rec): counts[5]}
    total_dominant = 0
    for couple, number in couples.items():
        father, mother = couple
        probabilities = md.Locus.mate(father, mother)
        dominant_probability = probabilities[dom] + probabilities[het]
        total_dominant += offspring_number * dominant_probability * number
    print(total_dominant)


if __name__ == '__main__':
    main()