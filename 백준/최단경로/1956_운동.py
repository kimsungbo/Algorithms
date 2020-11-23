# 1956 운동
# 최단거리 알고리즘을 응용하여 최단 사이클을 찾는 문제

import sys

INF = sys.maxsize
input = sys.stdin.readline
V, E = map(int, input().split())

def FloydWarshall(graph):
    dist = [[INF] * (V+1) for i in range(V+1)]
    
    for i in range(V+1):
        for j in range(V+1):
            # 다시 원래 마을로 돌아와야 하기 때문에 시작정점에서 자기 자신에게 가는것 0 으로 생각 X
            if graph[i][j] != 0:
                dist[i][j] = graph[i][j]
            
    for k in range(V+1):
        for i in range(V+1):
            for j in range(V+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

graph = [[0] * (V+1) for i in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
min_dist = FloydWarshall(graph)

result = INF

for i in range(1, V+1):
    result = min(result, min_dist[i][i])
    
if result == INF:
    print(-1)
else:
    print(result)
    
