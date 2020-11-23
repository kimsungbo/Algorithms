import heapq

def solution(scoville, K):
    heap = []
    
    for scov in scoville:
        heapq.heappush(heap, scov)
    answer = 0
    
    
    while heap[0] < K:
        
        if len(heap) == 1:
            return -1
        
        x = heapq.heappop(heap)
        
        if x < K:
            y = heapq.heappop(heap)
            
            heapq.heappush(heap, x + y * 2)
            answer += 1
            
            
            
    return answer