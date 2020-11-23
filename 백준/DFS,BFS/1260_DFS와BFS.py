# 1260 DFS와 BFS

from collections import deque

n, m, v = map(int, input().split())

graph = dict()
graph = [set([]) for _ in range(n+1)]
 
for i in range(m):
    a, b= map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

# 깊이 우선 탐색
def dfs(graph, start_node):
    visited = []
    
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)  
            stack.extend(sorted(graph[node], reverse=True))
    
    return visited

# 너비 우선 탐색
def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))
    return visited

dfs_sequence = dfs(graph, v)
bfs_sequence = bfs(graph, v)

for x in dfs_sequence:
    print(x, end = " " )

print()
    
for x in bfs_sequence:
    print(x, end = " " )