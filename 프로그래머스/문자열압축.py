from collections import deque

def zip(length, s):
    
    new_s = ""
    s = deque([s[i:i+length] for i in range(0, len(s), length)])
    while s:
        x = s.popleft()
        count = 1
        while s:               
            y = s[0]    
            if x == y:
                s.popleft()
                count += 1
            elif x != y:
                break
                
        if count == 1:
            new_s += x
        elif count > 1:
            new_s += str(count) + x
    return len(new_s)           
                 

def solution(s):
    answer = []
    
    for i in range(1, len(s)):
        answer.append(zip(i, s))
        
    if answer:
        return min(answer)
    else:
        return len(s)