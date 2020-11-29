def solution(n, s):
    if n > s: return [-1]
    answer = [s // n for _ in range(n)]
    
    remainder = s - sum(answer)
    
    idx = len(answer) - 1
    while remainder != 0:
        answer[idx] += 1
        remainder -= 1
        idx -= 1
    
    print(answer)
    return answer