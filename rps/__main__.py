import argparse
import rps.sequence_problems.counting_DNA_nucleotides as counting_dna_nucleotides

PROBLEMS = {
    "counting-dna-nucleotides": counting_dna_nucleotides.main
}
# TODO - add other modules


def solve_problem(name):
    action = PROBLEMS[name]
    action()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("problem", help="Choose which problem to solve")
    args = parser.parse_args()
    solve_problem(args.problem)


if __name__ == '__main__':
    main()
