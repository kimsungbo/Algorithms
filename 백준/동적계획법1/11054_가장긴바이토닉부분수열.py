# 11054 가장 긴 바이토닉 부분 수열

n = int(input())

seq = list(map(int, input().split()))

bigger_dp = [0 for i in range(n)]
smaller_dp = [0 for i in  range(n)]


for i in range(n):
    num = seq[i]
    maximum = 0
    for j in range(i):
        if seq[j] < num:
            if bigger_dp[j] > maximum:
                maximum = bigger_dp[j]
    bigger_dp[i] = maximum + 1
    
for i in range(n-1, -1, -1):
    num = seq[i]
    maximum = 0
    for j in range(n-1, i, -1):
        if seq[j] < num:
            if smaller_dp[j] > maximum:
                maximum = smaller_dp[j]
                
    smaller_dp[i] = maximum + 1


final_dp = [bigger_dp[i] + smaller_dp[i] for i in range(len(smaller_dp))]

print(max(final_dp) - 1)