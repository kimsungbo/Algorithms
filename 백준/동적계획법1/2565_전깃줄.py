# 2565 전깃줄

# 전깃줄

n = int(input())

wires = []
for i in range(n):
    wires.append(list(map(int, input().split())))
    
# print(wires)

wires = sorted(wires, key = lambda x: x[0])
# print(wires)


b_wires = [i[1] for i in wires]
# print(b_wires)

dp = [0 for i in range(n)]

for i in range(n):
    num = b_wires[i]
    maximum = 0
    for j in range(i):
        if b_wires[j] < num:
            if dp[j] > maximum:
                maximum = dp[j]
    dp[i] = maximum + 1
    
# print(dp)

print(n -max(dp))