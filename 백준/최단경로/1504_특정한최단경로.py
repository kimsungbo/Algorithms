# 1504 특정한 최단 경로
# 규칙을 만족하는 최단거리를 구하는 문제

# 특정한 최단경로

import sys
import heapq

input = sys.stdin.readline

INF = sys.maxsize

# 정점갯수 v, 간선갯수 e
V, E = map(int, input().split())

#가중치테이블
heap = []
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

v1, v2 = map(int, input().split())


def Dijkstra(start):
    # 시작점에서 자기 자신까지는 가중치 0
    dp = [INF] * (V+1)

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
                
first_v1 = Dijkstra(1)[v1]
first_v2 = Dijkstra(1)[v2]
v1_v2 = Dijkstra(v1)[v2]
v2_v1 = Dijkstra(v2)[v1]
v2_last = Dijkstra(v2)[-1]
v1_last = Dijkstra(v1)[-1]

first_v1_v2_lst = first_v1 + v1_v2 + v2_last
first_v2_v1_lst = first_v2 + v2_v1 + v1_last

shortest = min(first_v1_v2_lst, first_v2_v1_lst)

if shortest < INF:
    print(shortest)
    
else:
    print(-1)