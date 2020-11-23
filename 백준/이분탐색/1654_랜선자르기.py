# 1654 랜선 자르기
# parametric search
# 이분탐색을 응용하여 최솟값이나 최댓값 찾기

import sys
input = sys.stdin.readline

K, N = map(int, input().split())

lan_list = []
for i in range(K):
    lan_list.append(int(input()))
    
start = 1
end = max(lan_list)

while start <= end:
    mid = (start+ end) // 2
    
    num_lan = 0
    for i in lan_list:
        num_lan += i // mid
        
        
    if num_lan >= N:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)