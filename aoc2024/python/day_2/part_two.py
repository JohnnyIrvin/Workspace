#!/usr/bin/env python3

pop = lambda items: items.pop(0) if items else None

def is_safe(report: list[int]) -> bool:    
    for index in range(1, len(report)):
        window = report[index - 1: index + 2]
        last, value, next = pop(window), pop(window), pop(window)
        
        rules = [
            lambda: abs(value - last) in range(1, 4),
            lambda: (last < value) == (value < next) if next else True
        ]
        
        if any(not rule() for rule in rules):
            return False
    
    return True

safe_count: int = 0

with open('input.txt') as file:
    for line in file:
        record = list(map(int, line.strip().split(' ')))
        if is_safe(record):
            safe_count += 1
            continue
        
        for index in range(0, len(record)):
            copy = record[:index] + record[index + 1:]
            if is_safe(copy):
                safe_count += 1
                break

print(safe_count)