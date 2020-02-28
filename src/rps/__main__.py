import argparse
import sys
from typing import List

from rps.sequence_problems.counting_dna_nucleotides import count_nucleotides
from rps.sequence_problems.calculating_protein_mass import calculate_mass
from rps.sequence_problems.complementing_a_strand_of_dna import complement_dna
from rps.sequence_problems.computing_gc_content import calculate_max_gc_content
from rps.sequence_problems.consensus_and_profile import get_consensus_and_matrix
from rps.sequence_problems.counting_point_mutations import get_hamming_distance
from rps.sequence_problems.finding_a_motif_in_dna import get_motif_positions
from rps.sequence_problems.finding_a_shared_motif import longest_substring
from rps.sequence_problems.open_reading_frames import get_possible_proteins
from rps.sequence_problems.rna_splicing import splice_and_translate
from rps.sequence_problems.transcribing_dna_into_rna import transcribe
from rps.sequence_problems.transitions_and_transversions import calculate_tt_ratio
from rps.sequence_problems.translating_rna_into_protein import translate_dna

from rps.dynamic_programming_problems.rabbits_and_recurrence_relations import count_rabbits
from rps.dynamic_programming_problems.mortal_fibonacci_rabbits import count_mortal_rabbits

PROBLEMS = {
    "calculating-protein-mass": calculate_mass,
    "counting-dna-nucleotides": count_nucleotides,
    "complementing-a-strand-of-dna": complement_dna,
    "computing_gc_content": calculate_max_gc_content,
    "consensus-and-profile": get_consensus_and_matrix,
    "counting-point-mutations": get_hamming_distance,
    "finding-a-motif-in-dna": get_motif_positions,
    "finding-a-shared-motif": longest_substring,
    "open-reading-frames": get_possible_proteins,
    "rna-splicing": splice_and_translate,
    "transcribing-dna-into-rna": transcribe,
    "transitions-and-transversions": calculate_tt_ratio,
    "translating-rna-into-protein": translate_dna,
    "rabbits-and-recurrence-relations": count_rabbits,
    "mortal-fibonacci-rabbits": count_mortal_rabbits
}


# TODO - add other modules


def main():
    problem, input_file, output_file = parse_arguments()
    result = solve_problem(problem, data=get_data(input_file.name))
    print_result(result, output_file)


def parse_arguments():
    parser = argparse.ArgumentParser(description="Solver for rosalind problems")
    parser.add_argument("problem", help="Choose which problem to solve", choices=PROBLEMS.keys())
    parser.add_argument('input', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('output', nargs='?', type=argparse.FileType('r'), default=sys.stdout)
    args = parser.parse_args()
    return args.problem, args.input, args.output


def get_data(file) -> List[str]:
    data = [line.strip('\n') for line in file.readlines()]
    return data


def solve_problem(name, data):
    action = PROBLEMS[name]
    result = action(data)
    return result


def print_result(result, file):
    file.write(result)


if __name__ == '__main__':
    main()
