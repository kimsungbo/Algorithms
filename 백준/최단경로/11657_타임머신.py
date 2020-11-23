# 11657 타임머신
# 벨만 포드 알고리즘
# negative weight가 있을때 최단거리를 찾을 수 있게 해줌
# edge를 기준으로 모든 정점을 가는 최단거리를 찾음
# 정점갯수 = V라면, 모든 정점을 방문하려면 적어도 V-1번 방문해야 모든 정점 방문가능
#  -> 모든 edge들을 V-1번 보면서 각 정점의 최단거리를 찾음


import sys
import heapq

# input = sys.stdin.readline

INF = sys.maxsize

V, E = map(int, input().split())

graph = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph.append((u, v, w))
    

def BellmanFord(graph, start):  
  
    dist = [INF] * (V+1)
    dist[start] = 0
  
    for _ in range(V - 1):  
        for u, v, w in graph:  
            print(u, v, w)
            if dist[u] != INF and dist[u] + w < dist[v]:  
                dist[v] = dist[u] + w  
                
            print(dist)
  
    # 음의 사이클이 있는경우 -1
    for u, v, w in graph:  
        if dist[u] != INF and dist[u] + w < dist[v]:  
            return -1
                          
    return dist
        
min_dist = BellmanFord(graph, 1)

if min_dist == -1:
    print(-1)
else:
    for dist in min_dist[2:]:
        if dist == INF:
            print(-1)
        else:
            print(dist)