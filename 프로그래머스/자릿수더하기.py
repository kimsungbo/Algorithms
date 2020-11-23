def solution(n):
    n = str(n)
    n = [int(n[i]) for i in range(len(n))]
    
    return sum(n)