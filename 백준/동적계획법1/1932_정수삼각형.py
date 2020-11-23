# 1932 정수 삼각형
# 각 층의 모든 칸마다 최댓값을 저장하면서 동적 계획법으로 푸는 문제

import sys
input = sys.stdin.readline

n = int(input())

num_list = []

for i in range(n):
    num_list.append(list(map(int, input().split())))
    
for i in range(1, n):
    
    for j in range(0, len(num_list[i])):
        # 삼각형의 왼쪽끝에 있을경우 = 자기자신 + 전줄의 왼쪽끝값
        if j == 0:
            num_list[i][j] = num_list[i][j] + num_list[i-1][j]
        # 삼각형의 오른쪽 끝에 있을 경우 = 자기 자신 + 전줄의 오른쪽 끝값
        elif i == j:
            num_list[i][j] = num_list[i][j] + num_list[i-1][j-1]
        # 삼각형 왼쪽이나 오른쪽 끝이 아닐경우 = 자기자신 + max(전줄 자신의 왼쪽이나 자신의 오른쪽중 큰값)
        else:
            num_list[i][j] = num_list[i][j] + max(num_list[i-1][j-1], num_list[i-1][j])

print(max(num_list[n-1]))