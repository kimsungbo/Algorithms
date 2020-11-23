# 10866 덱

import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
# n = int(input())
queue = deque()

def push_front(x):
    queue.appendleft(x)

def push_back(x):
    queue.append(x)

def pop_front():
    if not queue:
        print(-1)
    else:
        print(queue.popleft())

def pop_back():
    if not queue:
        print(-1)
    else:
        print(queue.pop())
    
def size():
    print(len(queue))
    
def empty():
    if not queue:
        print(1)
    else: 
        print(0)

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
    
    if command[0] == 'push_front':
        push_front(command[1])
    elif command[0] == 'push_back':
        push_back(command[1])
    elif command[0] == 'pop_front':
        pop_front()
    elif command[0] == 'pop_back':
        pop_back()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'front':
        front()
    elif command[0] == 'back':
        back()