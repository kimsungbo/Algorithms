import heapq

def solution(n, works):
    
    if sum(works) < n:
        return 0
    
    heap = []
    
    for work in works:
        heapq.heappush(heap, -1 * work)
    
    print(heap)
    
    while n != 0:
        x = heapq.heappop(heap)
        heapq.heappush(heap, x + 1)
        n -= 1
        
    heap = [(-1 * i) ** 2 for i in heap]
    
    return sum(heap)
    
    
    