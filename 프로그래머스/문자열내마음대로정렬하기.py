def solution(strings, n):
    for i in range(len(strings)):
        strings[i] = list(strings[i])
        
    strings = sorted(strings, key = lambda x: (x[n], x))
    
    for i in range(len(strings)):
        strings[i] = ''.join(strings[i])

    return strings