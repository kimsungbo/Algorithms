# 1904 01 타일
# 점화식의 값을 특정 상수로 나눈 나머지를 구하는 문제

n = int(input())

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for k in range(3, n+1):
    dp[k] = (dp[k-1] + dp[k-2]) % 15746

print(dp[n])