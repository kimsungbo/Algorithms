def is_palindrome(string):
    return string == string[::-1]


def solution(s):
    
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    
    for i in range(len(s), 1, -1):
        for j in range(0, len(s)-i + 1):
            if is_palindrome(s[j:j+i]):
                return i
    return 1