"""
A module responsible for loading data from files and saving it
"""
from typing import List


def get_data(filepath) -> List[str]:
    with open(filepath, 'r') as file:
        data = [line.strip('\n') for line in file.readlines()]
    return data
