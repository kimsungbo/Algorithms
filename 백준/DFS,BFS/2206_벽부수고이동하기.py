# 2206 벽 부수고 이동하기
# 현재상태를 정점으로 표현하여 그래프를 만들고 최단거리를 구하는 문제

import sys
import heapq

n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input())))
    

# visited[x][y][벽 파괴 yes/no]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

def bfs(start, matrix, visited, n, m):
    
    queue = []
    
    dx = [-1, 1, 0 , 0]
    dy = [0, 0, 1, -1]
    
    # 최단거리일수록 우선으로 뽑기위해 heap 사용
    heapq.heappush(queue, start)
    
    while queue:
        
        count, wall, x, y = heapq.heappop(queue)
        visited[x][y][wall] = 1
        
        # 목적지에 도착했을 경우
        if x == n - 1 and y == m - 1:
            return count
        
        dx = [-1, 1, 0 , 0]
        dy = [0, 0, 1, -1]
   
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # out of index 검사에 충족하고
            if  0 <= nx < n and m > ny >= 0:
                # 아직 방문하지 않았고
                if visited[nx][ny][wall] == 0:                
                    # 이동할수 있거나/ 이동하지 않았지만 벽을 아직 한번 부술 수 있는경우에
                    if matrix[nx][ny] == 0 or (matrix[nx][ny] == 1 and wall == 0):
                        #방문한다
                        visited[nx][ny][wall] = 1
                    
                        # 벽 부술 경우
                        if matrix[nx][ny] == 1:
                            heapq.heappush(queue, (count + 1, 1 - wall, nx, ny))
                        # 벽 부수지 않을 경우
                        else:
                            heapq.heappush(queue, (count + 1, wall, nx, ny))

                        
    return -1

print(bfs((1,0,0,0), matrix, visited, n, m))
            