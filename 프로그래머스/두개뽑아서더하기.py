from itertools import combinations

def solution(numbers):
    
    combi = list(combinations(numbers, 2))
    
    combi = [combi[i][0] + combi[i][1] for i in range(len(combi))]
    
    return sorted(list(set(combi)))