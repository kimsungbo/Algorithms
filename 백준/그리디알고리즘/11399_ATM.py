# 11399 ATM
# 기다리는 시간의 합을 최소화하는 문제

n = int(input())

waiting_list = sorted(list(map(int, input().split())))

ans = 0
for x in range(len(waiting_list) + 1):
    ans += sum(waiting_list[0:x])

print(ans)