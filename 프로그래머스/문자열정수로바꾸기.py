def solution(s):
    
    if s[0] == '-':
        return -1 * int(''.join(s[1:]))
    else:
        return int(''.join(s))