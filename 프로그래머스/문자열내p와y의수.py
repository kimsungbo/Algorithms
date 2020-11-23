def solution(s):
    s = s.lower()
    
    if 'p' not in s and 'y' not in s:
        return True
    
    if s.count('p') == s.count('y'):
        return True
    else:
        return False