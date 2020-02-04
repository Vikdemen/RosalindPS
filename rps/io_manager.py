"""
A module responsible for loading data from files and saving it
"""

from typing import List


def read_file(filename: str) -> List[str]:
    """
    :param filename: a file name with extension. Searches in the same folder.
    :return: A list of strings, each for a line in a text fine
    """
    with open(filename, 'r') as file:
        data = file.readlines()
    # sanitises the data, removing newlines

    data = [line.replace('\n', '') for line in data]
    return data
# TODO - add other unprintable characters


def parse_fasta(data: List[str]):
    """
    :param data: Takes several sequences, where first line is fasta tag and next are multi-line sequence.
    :return:
    """
    sequences = []
    i = -1
    for line in data:
        if line.startswith('>'):
            sequences.append([line[1:], ""])
            i += 1
        else:
            sequences[i][1] += line

    # throws error if the first line doesn't start with tag

    sequences = [(s[1], s[0]) for s in sequences]
    return sequences
