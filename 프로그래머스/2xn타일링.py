def solution(n):
    dp = [0] * 60001
    dp[1] = 1
    dp[2] = 2
    
    for k in range(3, n+1):
        dp[k] = (dp[k-1] + dp[k-2]) % 1000000007
        
    return dp[k]
    