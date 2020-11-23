from collections import deque

def solution(s):
    
    if s == '':
        return ''
    
    string = []
    s = deque(s)
    temp_string = ''
    while s:
        if s[0] != " ":
            temp_string += s.popleft()
        elif s[0] == " ":
            string.append(temp_string)
            string.append(s.popleft())
            temp_string = ''
    string.append(temp_string)


    answer = ''
    for word in string:
        if word != " " and word != '':
            answer += word[0].upper() + word[1:].lower()
        elif word == " ":
            answer += " "
            
    return answer