# 1912 연속합
# 가장 큰 연속합을 구하는 문제

# 연속합

n = int(input())
seq = list(map(int, input().split()))
dp = [0 for i in range(n)]

for i in range(len(seq)):
    if i == 0:
        dp[i] = seq[i]
    else:
        dp[i] = max(dp[i - 1] + seq[i], seq[i])
        
print(max(dp))