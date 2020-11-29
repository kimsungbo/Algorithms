import math
def solution(n, k):
    temp = [i for i in range(1, n+1)]
    answer = []
    
    for i in range(n, 0, -1):
        facto = math.factorial(i-1)
        answer.append(temp.pop((k-1) // facto))
        k = k % facto
        
    return answer