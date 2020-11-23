# 1655 가운데를 말해요
# 우선순위 큐를 응용하여 중앙값을 빠르게 찾는 문제

import heapq
import sys

x = int(input())

max_heap = []
min_heap = []

for i in range(x):
    n = int(sys.stdin.readline())

    if len(max_heap) == 0:
        heapq.heappush(max_heap, (-n, n))

    elif len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-n, n))
    
    else:
        heapq.heappush(min_heap, n)
        
    if len(max_heap) != 0 and len(min_heap) != 0 and max_heap[0][1] > min_heap[0]:
        maximum = max_heap[0][1]
        minimum = min_heap[0]
        heapq.heapreplace(max_heap, (-minimum, minimum))
        heapq.heapreplace(min_heap, maximum)
        
    print(max_heap[0][1])