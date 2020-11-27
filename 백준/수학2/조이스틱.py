from collections import deque

def solution(name):
    answer = 0
    index = 0
    temp = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    
    print(temp)
    while True:
        answer += temp[index]
        temp[index] = 0
        
        if sum(temp) == 0:
            return answer
        
        left = 1
        right = 1
        
        while temp[index - left] == 0:
            left += 1
            
        while temp[index + right ] == 0:
            right += 1
            
        answer += left if left < right else right
        index += -left if left < right else right
        
        print(index)
        print(temp)
    
    return answer