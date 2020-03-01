from typing import List

from rps.sequence_problems.sequences import DNA


def parse_fasta(data: List[str]) -> List[DNA]:
    """
    :param data: Takes several lines, where first line is fasta tag and next are multi-line sequence.
    :return: a list of DNA sequences with tags
    """
    # only tagged sequence_problems allowed
    if not data[0].startswith('>'):
        raise ValueError('Sequences must be in fasta format')

    # creates a lists of tuples where fist item is sequence, second item is tag
    sequences = []
    i = -1
    for line in data:
        # creates a new sequence with tag and empty string
        if line.startswith('>'):
            # removes '>' at the start of tag
            edited = line[1:]
            sequences.append(["", edited])
            i += 1
        # concatenates subsequent lines to a sequence until is reached
        else:
            sequences[i][0] += line
    sequences = [DNA(seq[0], seq[1]) for seq in sequences]
    return sequences
