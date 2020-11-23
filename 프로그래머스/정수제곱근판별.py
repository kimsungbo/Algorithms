import math

def solution(n):
    
    for i in range(1, round(math.sqrt(n)) + 1):
        if n == (i ** 2):
            return (i+1) ** 2
    
    return -1