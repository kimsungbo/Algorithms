# 10828 스택

import sys

n = int(sys.stdin.readline().rstrip())
stack = []

def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)
    
def size():
    print(len(stack))
    
def empty():
    if not stack:
        print(1)
    else: 
        print(0)
        
def pop():
    if stack:
        print(stack[-1])
        del stack[-1]
    else:
        print(-1)

def push(x):
    stack.append(x)
        
    
command = []
for i in range(n):
    command = sys.stdin.readline().rstrip().split()
    
    if(len(command) == 1):
        if command[0] == 'pop':
            pop()
        elif command[0] == 'size':
            size()
        elif command[0] == 'empty':
            empty()
        elif command[0] == 'top':
            top()
    
    else:
        if command[0] == 'push':
            push(command[1])