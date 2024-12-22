#!/usr/bin/env python3
from typing import Optional

def is_safe(report: list[int]) -> bool:
    inc: Optional[bool] = None
    last: Optional[int] = None    
    
    for i in report:
        i = int(i)
        
        if last is None:
            last = i
            continue
        
        if inc is None:
            inc = i > last
            
        if (inc and i < last) or (not inc and i > last):
            return False
        
        abs_diff = abs(i - last)
        if abs_diff > 3 or abs_diff < 1:
            return False
        
        last = i
    
    return True


safe_count = sum(1 for line in open('input.txt') if is_safe(line.strip().split(' ')))
        
print(safe_count)