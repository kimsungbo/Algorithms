from collections import deque

def solution(s):
    
    s = s[2:-2]
    
    
    list = s.split("},{")
    
    for i in range(len(list)):
        temp = list[i].split(",")
        list[i] = [int(temp[j]) for j in range(len(temp))]
        
    
    list = sorted(list, key = lambda x:len(x))
    
    list = deque(list)
    stack = [list.popleft()[0]]
    
    while list:
        temp = list.popleft()
        
        for i in range(len(temp)):
            if temp[i] not in stack:
                stack.append(temp[i])
                
    return stack