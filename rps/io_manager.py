"""
A module responsible for loading data from files and saving it
"""

from typing import List


def read_file(filename: str) -> List[str]:
    """
    :param filename: a file name with extension. Searches in the same folder.
    :return: A list of strings, each for a line in a text fine. Newlines are stripped.
    """
    path = "../data/" + filename
    with open(path, 'r') as file:
        data = file.readlines()
    # sanitises the data, removing newlines
    # windows-style newlines are automatically replaced by Python
    data = [line.replace('\n', '') for line in data]
    return data


def parse_fasta(data: List[str]):
    """
    :param data: Takes several sequence_problems, where first line is fasta tag and next are multi-line sequence.
    :return: a list of 2-item lists, where first is sequence and second is tag
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
    return sequences
