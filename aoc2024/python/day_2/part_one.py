#!/usr/bin/env python3

pop = lambda items: items.pop(0) if items else None

def is_safe(report: list[int]) -> bool:    
    for index in range(1, len(report)):
        window = report[index - 1: index + 2]
        last, value, next = pop(window), pop(window), pop(window)
            
        if next and (last < value) != (value < next):
            return False
        
        if abs(value - last) not in range(1, 4):
            return False
    
    return True

safe_count = sum(
    1 for line
    in open('input.txt')
    if is_safe(
        list(map(int, line.strip().split(' ')))
    )
)
        
print(safe_count)
