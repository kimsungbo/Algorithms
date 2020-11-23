# 4949 균형잡힌 세상

import sys

def is_vps(orgstring):
    stack = []
    
    string = []
    for i in range(0, len(orgstring)):
        if(orgstring[i] in ['(', ')', '[', ']']):
            string.append(orgstring[i])
    
    for i in range(len(string)-1, -1, -1):
        if string[i] == ')' or string[i] == ']':
            stack.append(string[i])
        elif string[i] == '(' and not stack:
            return "no"
        elif string[i] == '[' and not stack:
            return "no"
        elif string[i] == '(' and stack[-1] == ')':
            stack.pop()
        elif string[i] == '[' and stack[-1] == ']':
            stack.pop()
        else:
            return "no"
    
    if not stack:
        return "yes"
    else:
        return "no"
                

while True:
    string = list(str(input()))
    if string[0] =='.':
        break
    ans = is_vps(string)
    print(ans)
