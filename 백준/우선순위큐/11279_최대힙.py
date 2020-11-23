# 11279 최대 힙
# 최댓값을 빠르게 뽑는 자료구조

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
        heapq.heappush(num_list, (-num, num))