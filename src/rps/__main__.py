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
    "translating-rna-into-protein": translate_dna
}


# TODO - add other modules


def solve_problem(name, data):
    action = PROBLEMS[name]
    result = action(data)
    return result


def get_data(filepath) -> List[str]:
    with open(filepath, 'r') as file:
        data = [line.strip('\n') for line in file.readlines()]
    return data


def print_result(result):
    print(result)


def main():
    args = parse_arguments()
    result = solve_problem(args.problem, data=get_data(args.input.name))
    print_result(result)


def parse_arguments():
    parser = argparse.ArgumentParser(description="Solver for rosalind problems")
    parser.add_argument("problem", help="Choose which problem to solve", choices=PROBLEMS.keys())
    parser.add_argument('input', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('output', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
