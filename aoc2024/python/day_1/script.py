#!/usr/bin/env python3
import argparse
import pathlib

DESCRIPTION = \
    """
    Advent of Code 2024, Day 1, Part Two
    
    This script is used to solve the first day of the Advent of Code 2024, Part Two.
    
    The challenges requires:
    
    - Use list one to create a dictionary with keys and values to zero
    - Loop through list two and check if the value is in the dictionary
    - If the value is in the dictionary, increment the value by one
    - For each key multiply it by the value and sum the results
    """
    
def read_file(file: pathlib.Path) -> tuple[list[int], list[int]]:
    """
    Reads a file and returns a tuple of two lists of integers.
    
    :param file: The file to read
    :return: A tuple of two lists of integers
    """
    assert file.exists(), f'File {file} does not exist'
    
    separator: str = ' ' * 3
    list1, list2 = [], []
    
    with file.open('r') as f:
        for line in f:
            entry1, entry2 = line.split(separator)
            list1.append(int(entry1))
            list2.append(int(entry2))

    return list1, list2

def main() -> int:
    # Requires a file for target
    parser = argparse.ArgumentParser(description=DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('target', type=str, help='File containing the target')
    args = parser.parse_args()
    
    # Read the file
    target = pathlib.Path(args.target)
    list1, list2 = read_file(target)
    
    
    return 0

if __name__ == '__main__':
    exit(main())
