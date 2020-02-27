import argparse
import sys
from typing import List

from rps.sequence_problems import counting_dna_nucleotides, complementing_a_strand_of_dna, computing_gc_content

PROBLEMS = {
    "counting-dna-nucleotides": counting_dna_nucleotides.count_nucleotides,
    "complementing-a-strand-of-dna": complementing_a_strand_of_dna.main,
    "computing_gc_content": computing_gc_content.main
}


# TODO - add other modules


def solve_problem(name, data):
    action = PROBLEMS[name]
    result = action(data)
    return result


def get_data(filepath) -> List[str]:
    with open(filepath, 'r') as file:
        data = file.readlines()
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
