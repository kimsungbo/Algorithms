# 11404 플로이드
# 플로이드 와셜 알고리즘
# 모든 정점 사이의 최단경로를 찾음
# 1. 하나의 정점에서 바로 갈 수 있으면 최소비용, 갈 수 없다면 INF
# 2. 3중 loop를 사용하여 거쳐가는 정점을 선택한 후, 그 정점을 거쳐가서 비용이 줄어들면 값을 바꿔줌
# 3. 위의 과정 반복해 모든 정점 사이의 최단경로 탐색

import sys

input = sys.stdin.readline

INF = sys.maxsize

def FloydWarshall(graph):
    dist = [[INF] * (V+1) for i in range(V+1)]
    
    for i in range(V+1):
        for j in range(V+1):
            # 하나의 정점에서 바로 갈 수 있으면 최소비용
            if graph[i][j] != 0:
                dist[i][j] = graph[i][j]
            # 자기자신에게 가는데에는 가중치 0
            elif i == j:
                dist[i][j] = 0
            
    for k in range(V+1):
        for i in range(V+1):
            for j in range(V+1):
                # i->j로 이동하는데 i->j->k로 이동하는게 더 적은 비용이 들경우 업데이트
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    return dist

V = int(input())

E = int(input())

graph = [[0] * (V+1) for i in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    if graph[a][b] == 0 or graph[a][b] > c:
        graph[a][b] = c
    
                    
    
min_dist = FloydWarshall(graph)

for i in range(1, len(min_dist)):
    for j in range(1, len(min_dist[i])):
        if min_dist[i][j] != INF:
            print(min_dist[i][j], end = " ")
        else:
            print(0, end = " ")
    print()