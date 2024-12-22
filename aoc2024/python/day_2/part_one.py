#!/usr/bin/env python3
def is_safe(report: list[int]) -> bool:    
    for index in range(1, len(report)):
        last = report[index - 1]
        value = report[index]
        next = report[index + 1] if index + 1 < len(report) else None
            
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