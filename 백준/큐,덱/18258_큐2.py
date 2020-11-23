# 18258 큐2
# O(1)

import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
# n = int(input())
queue = deque()

def push(x):
    queue.append(x)
    
def size():
    print(len(queue))
    
def empty():
    if not queue:
        print(1)
    else: 
        print(0)
        
def pop():
    if queue:
        print(queue[0])
        queue.popleft()
    else:
        print(-1)

def front():
    if not queue:
        print(-1)
    else:
        print(queue[0])

def back():
    if not queue:
        print(-1)
    else:
        print(queue[-1])
        
    
command = []
for i in range(n):
    command = sys.stdin.readline().rstrip().split()
#     command = list(map(str, input().split()))
    
    if command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'front':
        front()
    elif command[0] == 'back':
        back()
    elif command[0] == 'push':
        push(command[1])