def solution(n):
    
    dp = [0] * 2001
    
    dp[1] = 1
    dp[2] = 2
    
    for k in range(3, n+1):
        dp[k] = (dp[k-1] + dp[k-2]) %  1234567
        
    return dp[n]