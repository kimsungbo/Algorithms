# 1149 RGB거리
# i번째 집을 각각의 색으로 칠할 때, 1 ~ i 번째 집을 모두 칠하는 최소 비용으로 부분문제 정의

import sys
input = sys.stdin.readline

n = int(input())

# 집을 각각 빨, 초, 파로 칠할때 드는 비용
matrix = [[0] * 3 for i in range(n)]

for i in range(n):
    matrix[i][0], matrix[i][1], matrix[i][2] = map(int, input().split())
    
dp = [[0] * 3 for i in range(n)]

for i in range(n):
    # 첫집은 그대로의 비용이 듬
    if i == 0:
        dp[i] = matrix[i]
        
    else:
        # 집을 빨간색으로 칠할경우 = 빨간색으로 칠하는 비용 + min(전집을 초록이나 파랑 중 비용이 적게드는 색으로 칠함)
        dp[i][0] = matrix[i][0] + min(dp[i-1][1], dp[i-1][2])
        # 집을 초록색으로 칠할경우 = 초록색으로 칠하는 비용 + min(전집을 빨강이나 파랑 중 비용이 적게드는 색으로 칠함)
        dp[i][1] = matrix[i][1] + min(dp[i-1][0], dp[i-1][2])
        # 집을 파란색으로 칠할경우 = 파란색으로 칠하는 비용 + min(전집을 빨강이나 초록 중 비용이 적게드는 색으로 칠함)
        dp[i][2] = matrix[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))