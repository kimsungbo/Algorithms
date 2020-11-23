# 1927 최소 힙
# 최솟값을 빠르게 뽑는 문제

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
            print(heapq.heappop(num_list))
    else:
        heapq.heappush(num_list, num)