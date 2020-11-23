# 11286 절댓값 힙
# 새로운 기준으로 뽑는 우선순위 큐를 만드는 문제

import heapq
import sys
n = int(input())

num_list = []
for i in range(n):
    num = int(sys.stdin.readline())
    
    if num == 0:
        if not num_list:
            print(0)
        else:
            print(heapq.heappop(num_list)[1])
    else:
        heapq.heappush(num_list, (abs(num), num))