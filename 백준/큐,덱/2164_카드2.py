# 2164 카드2
# 큐를 사용하여 동작을 구현하는 문제

from collections import deque

n = int(input())

queue = deque()
for i in range(1, n+1):
    queue.append(i)
    
card_left = n

while True:
    if card_left == 1:
        print(queue[0])
        break
        
    queue.popleft()
    queue.append(queue.popleft())
    card_left -= 1
    