from collections import deque

def solution(s):
    s = deque(s)
    stack = []
    
    if s.count('(') != s.count(')'):
        return False
    
    while s:
        bracket = s.popleft()
        
        if bracket == '(':
            stack.append('(')
        elif bracket == ')' and stack:
            if stack[-1] == '(':
                stack.pop()
                
    if stack:
        return False
    else:
        return True