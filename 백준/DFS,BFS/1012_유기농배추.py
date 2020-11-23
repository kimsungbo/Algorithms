# 1012 유기농 배추
# 땅의 모습이 아니라 배추의 위치가 주어지는 문제

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**8)


t = int(input())


def dfs(matrix, cnt, x, y):
    
    # 들렸으니 0 으로 바꿈
    matrix[x][y] = 0
    
    dx = [-1, 1, 0 , 0]
    dy = [0, 0, 1, -1]
   
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if matrix[nx][ny] == 1:
                cnt = dfs(matrix, cnt+1, nx, ny)
            
    return cnt

for i in range(t):
    m, n, k = map(int, input().split())
    
    matrix = [[0] * m for i in range(n)]
    
    
    for j in range(k):
        x, y = map(int, input().split())
        matrix[y][x] = 1
        
    ans = []
    for a in range(n):
        for b in range(m):
            if matrix[a][b] == 1:
                ans.append(dfs(matrix, 1, a, b))
            
    print(len(ans))