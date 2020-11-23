# 2606 바이러스
# bfs나 dfs로 그래프를 순회해서 방문할 수 있는 정점을 찾는 문제

from collections import deque

n = int(input())
m = int(input())

graph = dict()
graph = [set([]) for _ in range(n+1)]
 
for i in range(m):
    a, b= map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

def dfs(graph, start_node):
    visited = []
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)    
            stack.extend(sorted(graph[node], reverse=True))
    
    return visited

dfs_sequence = dfs(graph, 1)

print(len(dfs_sequence) - 1)