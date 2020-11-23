# 2156 포도주 시식
# 규칙에 따라 포도주를 마실 때, 최대로 마실 수  있는 포도주의 양을 구하는 문제

n = int(input())

wine_list = [0]
for i in range(n):
    wine_list.append(int(input()))
    
dp = [0]
dp.append(wine_list[1])

for i in range(2, n + 1):
    if i == 2:
        dp.append(wine_list[1] + wine_list[2])    
    else:
        dp.append(max(dp[i-1], dp[i-3] + wine_list[i-1] + wine_list[i], dp[i-2] + wine_list[i]))

print(dp[-1])