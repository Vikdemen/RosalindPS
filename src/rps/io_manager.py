"""
A module responsible for loading data from files and saving it
"""
from typing import List, Callable, Any
from pathlib import Path
from sequences import DNA
from functools import wraps


def read_file(filename: str) -> List[str]:
    """
    :param filename: a file name with extension. Searches in the same folder.
    :return: A list of strings, each for a line in a text fine. Newlines are stripped.
    """
    path = Path(Path(__file__).parent.parent, 'data', filename)
    with open(path, 'r') as file:
        data = file.readlines()
    # sanitises the data, removing newlines
    # windows-style newlines are automatically replaced by Python
    data = [line.replace('\n', '') for line in data]
    return data


def as_fasta(func: Callable[[List[DNA]], Any]) -> Callable[[List[str]], Any]:
    """
    :param func: Function that accepts a list of DNA sequences
    :return: Decorated function that accepts a list of lines from FASTA file
    """
    @wraps(func)
    def fasta_parsing(fasta_lines: List[str]):
        sequences = parse_fasta(fasta_lines)
        result = func(sequences)
        return result
    return fasta_parsing


def parse_fasta(data: List[str]) -> List[DNA]:
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
    sequences = [DNA(seq[0], seq[1]) for seq in sequences]
    return sequences


def single_line(func: Callable[[str], Any]) -> Callable[[List[str]], Any]:
    @wraps(func)
    def unpacking(line: List[str]):
        if len(line) != 1:
            raise ValueError("a single line is expected")
        content, = line
        result = func(content)
        return result
    return unpacking

