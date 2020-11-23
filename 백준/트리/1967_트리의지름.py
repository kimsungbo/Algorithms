# 1967 트리의 지름
# 가중치가 있는 트리의 지름을 구하는 문제

# 트리의 지름


import sys
import heapq
INF = sys.maxsize
# input = sys.stdin.readline

n = int(input())

heap = []
graph = [[] for _ in range( n+1)]

for i in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((w,v))
    graph[v].append((w, u))
        

def Dijkstra(start):
    # 시작점에서 자기 자신까지는 가중치 0
    dp = [INF] * (n+1)

    dp[start] = 0
    heapq.heappush(heap, (0, start))
    
    while heap:
        
        currentWeight, currentNode = heapq.heappop(heap)
        
        # 현재 가중치 테이블과 비교하여 더 큰 가중치면 무시
        if dp[currentNode] < currentWeight:
            continue
            
        for tempWeight, nextNode in graph[currentNode]:
            nextWeight = tempWeight + currentWeight
            # 다음 노드까지의 가중치가 현재 기록된 가중치보다 작으면 조건 성립
            if nextWeight < dp[nextNode]:
                # 가중치 테이블 업데이트
                dp[nextNode] = nextWeight
                # 다음 점까지의 가중치와 다음 점에 대한 튜플을 묶어 힙에 저장
                heapq.heappush(heap, (nextWeight, nextNode))
                
    return dp


di = Dijkstra(1)
        
print(max(Dijkstra(di.index(max(di[1:])))[1:]))  
