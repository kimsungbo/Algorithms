# 1463 1로 만들기
# 메모제이션으로 N을 1로 바꾸기 위해 주어진 연산을 몇 번 사용하는지 계산하는 문제

n = int(input())

dp = [[0] for i in range(n+1)]
dp[1] = 0

for i in range(2, n+1):
    num_cal = []

    # 그 전 연산값에 +1만 해주면 되기 때문에 i-1의 연산횟수에 +1만 해주면 됨    
    num_cal.append(dp[i-1] + 1)
    
    # 2로 나눠질경우 나누기2한값에 X2만해주면 되기때문에 i//2의 연산횟수에 +1만 해주면 됨
    if i % 2 == 0:
        num_cal.append(dp[i//2] + 1)
    # 3으로 나눠질경우 나누기 3한값에 X3만 해주면 되기 때문에 i // 3의 연산횟수에 +1만 해주면 됨
    if i % 3 == 0:
        num_cal.append(dp[i//3] + 1)
        
    # 위의 세 연산중 제일 연산횟수가 적은것을 고른다
    dp[i] = min(num_cal)
    
print(dp[n])