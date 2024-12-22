#!/usr/bin/env python3
import argparse

DESCRIPTION = \
    """
    Advent of Code 2024, Day 1
    
    This script is used to solve the first day of the Advent of Code 2024.
    
    The challenges requires:
    
    - Sorts each list of numbers from lowest to highest (ascending order)
    - Starting at index 0, compares the two lists of numbers.
    - The comparison is done by taking the absolute difference between the two numbers.
    - The differences are summed.
    - The sum is the answer to the challenge.
    
    Formula:
    
    sum(abs(a - b) for a, b in zip(list1, list2))
    """

def main() -> int:
    # Requires a file for target
    parser = argparse.ArgumentParser(description=DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('target', type=str, help='File containing the target')
    args = parser.parse_args()
    
    print(args.target)
    
    return 0

if __name__ == '__main__':
    exit(main())
