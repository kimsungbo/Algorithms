# 2579 계단 오르기
# i 번째 계단에 오를 때, 몇 개의 연속한 계단을 올랐는지를 고려하여 부분문제 정의

n = int(input())

stairs = []
dp = []

for i in range(n):
    stairs.append(int(input()))

# dp(n): n칸까지 올랐을때의 최댓값
# dp(n) = max(직전에 올라온 경우, 두칸전에 올라온 경우)

# 0번째 계단은 무조건 밟아야 함
dp.append(stairs[0])

for i in range(1, n):
    # 첫번째계단 = max(0번째계단+현재계단, 현재계단에 바로 올 경우)
    if i == 1:
        dp.append(max(dp[i-1] + stairs[i], stairs[i]))
    # 두번째 계단 = max(0번째계단 + 현재계단, 1번계단 + 현재계단)
    elif i == 2:
        dp.append(max(dp[i-2] + stairs[i], stairs[i-1] + stairs[i]))
    # max(직전에 올라온 경우, 두칸전에 올라온 경우)
    else:
        dp.append(max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i] + dp[i-2]))

print(dp[-1])