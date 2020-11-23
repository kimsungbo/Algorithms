# 10773 제로
# 가장 최근에 쓴 수를 지우는 문제

import sys

n = int(sys.stdin.readline().rstrip())
# n = int(input())

stack = []
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
#     num = int(input())
    if(num == 0):
        del stack[-1]
    else:
        stack.append(num)

print(sum(stack))