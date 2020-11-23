# 11053 가장 긴 증가하는 부분 수열
# LIS(Longest Increasing Subsequence)를 구하는 문제

a = int(input())

seq = list(map(int, input().split()))

dp = [0 for i in range(a)]


for i in range(a):
    num = seq[i]
    maximum = 0
    for j in range(i):
        if seq[j] < num:
            if dp[j] > maximum:
                maximum = dp[j]
    dp[i] = maximum + 1
    
print(max(dp))    