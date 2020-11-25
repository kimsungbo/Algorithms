def is_vps(string):
    stack = []
    for i in range(len(string)-1, -1, -1):
        if string[i] == ')':
            stack.append(string[i])
        elif string[i] == '(' and not stack:
            return False
        elif string[i] == '(' and stack[-1] == ')':
            stack.pop()
    
    if not stack:
        return True
    else:
        return False



def get_uv(p):
    u = ""
    v = ""
    
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
            
        if count == 0:
            return p[:i + 1], p[i+1:]

    return "", p

def solution(p):
    
    
    answer = ""
    
    if p == "" or is_vps(p) == True:
        return p
    else:
        u, v = get_uv(p)
        
        if is_vps(u) == True:
            answer += u + solution(v)
        else:
            answer = '(' + solution(v) + ')'
            u = u[1:-1]
            
            u = ''.join([")" if b == "(" else "(" for b in u])
            answer += u
            
    return answer
            
        