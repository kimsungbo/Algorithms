def solution(s):
    answer = []
    
    j = 0
    for i in range(len(s)):
        print(s[i])
        if j % 2 == 0:
            answer.append(s[i].upper())
        else:
            answer.append(s[i].lower())
        j += 1
            
        if s[i] == ' ':
            j = 0
            
    return ''.join(answer)