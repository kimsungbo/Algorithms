# 2178 미로 탐색
# bfs를 사용하여 최단거리 구하기

from collections import deque

n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input())))
    

visited = [[0] * m for _ in range(n)]

queue= deque([(0,0)])
visited[0][0] = 1
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
        
    #최종경로에 도착한경우
    if x == n-1 and y == m-1:
        print(visited[x][y])
        break
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))