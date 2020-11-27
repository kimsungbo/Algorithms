from itertools import combinations

def is_prime(x):
    if x != 1:
        for i in range(2, x):
            if(x % i == 0):
                return False
    else:
        return False
    return True

def solution(nums):
    answer = 0
    
    combi = list(combinations(nums, 3))
    
    for a, b, c in combi:
        if is_prime(a+b+c) == True:
            answer += 1
            
    return answer