def solution(s, n):
    
    answer = []
    for i in range(len(s)):
        
        if s[i] == ' ':
            answer.append(' ')
        else:
            temp = ord(s[i])
            temp2 = ord(s[i]) + n

            if 65 <= temp <= 90:
                if temp2 > 90:
                    temp2 -= 26

            elif 97 <= temp <= 122:
                if temp2 > 122:
                    temp2 -= 26
                
            answer.append(chr(temp2))
        
    return ''.join(answer)