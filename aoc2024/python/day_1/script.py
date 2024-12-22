#!/usr/bin/env python3
import argparse
import pathlib

DESCRIPTION = \
    """
    Advent of Code 2024, Day 1, Part Two
    
    This script is used to solve the first day of the Advent of Code 2024, Part Two.
    
    The challenges requires:
    
    - Sorts each list of numbers from lowest to highest (ascending order)
    - Starting at index 0, compares the two lists of numbers.
    - The comparison is done by taking the absolute difference between the two numbers.
    - The differences are summed.
    - The sum is the answer to the challenge.
    
    Formula:
    
    sum(abs(a - b) for a, b in zip(list1, list2))
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
    
    list1, list2 = sorted(list1), sorted(list2)
    total = sum(abs(a - b) for a, b in zip(list1, list2))
    
    print(f'The sum of the absolute differences between the two lists is {total}')
    
    return 0

if __name__ == '__main__':
    exit(main())
