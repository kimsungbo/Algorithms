# 1167 트리의 지름
# bfs나 dfs로 트리에서 가장 먼 두 점을 찾는 문제

# 트리의 지름 = 임의의 정점 x에서 가장 먼 정점 y를 찾은 후 정점 y에서
#              가장 먼 정점 z를 연결하는 경로


import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

n = int(input())

heap = []
graph = [[] for _ in range( n+1)]

for i in range(n):
    temp_list = list(map(int, input().split()))
    fromNode = temp_list[0]
    for j in range(1, len(temp_list) - 1, 2):
        graph[fromNode].append((temp_list[j+1], temp_list[j]))
        

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
