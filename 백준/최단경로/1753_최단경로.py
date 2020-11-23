# 1753 최단경로
# 다익스트라 알고리즘

# 다익스트라

import sys
import heapq

input = sys.stdin.readline

INF = sys.maxsize

# 정점갯수 v, 간선갯수 e
V, E = map(int, input().split())

# 시작노드 k
K = int(input())

#가중치테이블
dp = [INF] * (V+1)
heap = []
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w,v))
    


def Dijkstra(start):
    # 시작점에서 자기 자신까지는 가중치 0
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
                
                
Dijkstra(K)

for i in range(1,V+1):
    print("INF" if dp[i] == INF else dp[i])