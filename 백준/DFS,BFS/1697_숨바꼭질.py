# 1697 숨바꼭질
# bfs 최단거리

import sys
from collections import deque

n , k = map(int, input().split())

LIMIT = 100001
find = [0] * LIMIT


def solve(arr, n, k):
    queue = deque()
    queue.append(n)
    
    while queue:
        current = queue.popleft()
        
        # 현재위치가 동생의 위치일경우 종료
        if current == k:
            return arr[current]
        
        # x+1, x-1, x*2중
        for next in (current+1, current-1, current*2):
            # 다음 갈 장소가 limit 보다 작거나 이미 방문하지 않았을때만 방문
            if (0 <= next < LIMIT and arr[next] == 0):
                # 전에 움직였던것보다 한번더 움직여야하므로 +1
                arr[next] = arr[current] + 1
                queue.append(next)
                
                
print(solve(find, n, k))