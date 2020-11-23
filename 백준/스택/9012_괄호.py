# 9012 괄호
# 주어진 문자열이 올바른 괄효열인지 판단하는 문제

import sys

def is_vps(string):
    stack = []
    for i in range(len(string)-1, -1, -1):
        if string[i] == ')':
            stack.append(string[i])
        elif string[i] == '(' and not stack:
            return "NO"
        elif string[i] == '(' and stack[-1] == ')':
            stack.pop()
    
    if not stack:
        return "YES"
    else:
        return "NO"
                

# n = int(sys.stdin.readline().rstrip())
n = int(input())

for i in range(n):
    string = list(str(input()))
    ans = is_vps(string)
    print(ans)
