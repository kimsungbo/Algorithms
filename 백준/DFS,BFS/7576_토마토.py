# 7576 토마토
# bfs로 토마토를 익히는 문제

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

def bfs(n, m, tomatos):
    
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    
    days = -1
    
    while ripe:
        days += 1
        
        for item in range(len(ripe)):
            x, y = ripe.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx >= 0 and nx < m and ny >= 0 and ny < n and tomatos[nx][ny] == 0:
                    tomatos[nx][ny] = 1
                    ripe.append([nx, ny])
                    
                    
    for b in tomatos:
        if 0 in b:
            return -1
    return days

tomatos = []
ripe = deque()

for i in range(m):
    temp_list = list(map(int, input().split()))
    tomatos.append(temp_list)
    for j in range(n):
        if temp_list[j] == 1:
            ripe.append([i, j])

print(bfs(n, m, tomatos))