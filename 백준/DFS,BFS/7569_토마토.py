# 7569 토마토
# 3차원 배열에 저장된 토마토를 bfs로 익히는 문제

from collections import deque
import sys

input = sys.stdin.readline

m, n, h = map(int, input().split())

def bfs(m, n, h, tomatos):
    
    dx = [0, 0, 1, -1, 0, 0]
    dy = [-1, 1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    
    days = -1
    
    while ripe:
        days += 1
        
        for item in range(len(ripe)):
            z, x, y = ripe.popleft()
            
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                
                if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                    if tomatos[nz][nx][ny] == 0:
                        tomatos[nz][nx][ny] = tomatos[z][x][y] + 1
                        ripe.append([nz, nx, ny])
                        
                    elif tomatos[nz][nx][ny] == -1:
                        continue
                    

            
    for a in tomatos:
        for b in a:
            if 0 in b:
                return -1
    
    return days

tomatos = []
ripe = deque()

            
tomatos = [[list(map(int, input().split())) for i in range(n)] for depth in range(h)]


for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatos[i][j][k] == 1:
                ripe.append([i, j, k])
                

print(bfs(m, n, h, tomatos))