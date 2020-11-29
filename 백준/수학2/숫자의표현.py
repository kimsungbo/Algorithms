def solution(n):
    temp = 0
    answer = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if temp >= n:
                
                if temp == n:
                    answer += 1
                    temp = 0
                    break
                else:
                    temp = 0
                    break
            temp += j
            
            
    return answer + 1