# 2667 단지번호 붙이기
# 2차원 배열을 그래프로 표현해 순회하는 문제

import sys

n = int(input())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input())))



def dfs(matrix, cnt, x, y):
    
    # 들렸으니 0 으로 바꿈
    matrix[x][y] = 0
    
    # 좌우상하
    dx = [-1, 1, 0 , 0]
    dy = [0, 0, 1, -1]
   
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if matrix[nx][ny] == 1:
                cnt = dfs(matrix, cnt+1, nx, ny)
            
    return cnt
    
    
ans = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            ans.append(dfs(matrix, 1, i, j))
            
print(len(ans))

for i in sorted(ans):
    print(i)