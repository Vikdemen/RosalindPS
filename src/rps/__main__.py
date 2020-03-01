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

from rps.heredity_problems.mendels_first_law import calculate_dominant_probabilities
from rps.heredity_problems.calculating_expected_offspring import expected_dominant_offspring

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
    "mortal-fibonacci-rabbits": count_mortal_rabbits,
    "mendels-first-law": calculate_dominant_probabilities,
    "calculating-expected-offsprint": expected_dominant_offspring
}


def main():
    problem, input_file, output_file, silent = parse_arguments()
    if not silent:
        if input_file == sys.stdin:
            print("Please, input data and press CTRL+D")
        else:
            print("Loading data")
    result = solve_problem(problem, data=get_data(input_file))
    print_result(result, output_file)
    if not silent:
        print("Task finished")


def parse_arguments():
    """
    Parses command line arguments
    :return: Problem name, input file, output file, silent mode
    """
    # Takes in the problem name and optional --input and --output file
    # If no file path is provided, stdin/stdout is used
    # If "silent" options is chosen, print statements are deactivated
    parser = argparse.ArgumentParser(description="Helper program for Rosalind")
    parser.add_argument("problem", help="Choose which problem to solve", choices=PROBLEMS.keys())
    parser.add_argument('-i', '--input', help="File to read from", nargs='?',
                        type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('-o', '--output', help="File to write to", nargs='?',
                        type=argparse.FileType('w'), default=sys.stdout)
    parser.add_argument('-s', '--silent', help="Does not print additional messages", action="store_true")
    args = parser.parse_args()
    return args.problem, args.input, args.output, args.silent


def get_data(file) -> List[str]:
    data = file.readlines()
    cleaned_data = [line.strip('\n') for line in data]
    return cleaned_data


def solve_problem(name: str, data: List[str]) -> str:
    action = PROBLEMS[name]
    result = action(data)
    return result


def print_result(result: str, file):
    file.write(str(result))


if __name__ == '__main__':
    main()
