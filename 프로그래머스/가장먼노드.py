from collections import deque 

def bfs(graph, start_node, visited):
    count = 0
    queue = deque([(start_node, count)])
    
    
    while queue:
        (node, count) = queue.popleft()
        
        if visited[node] == -1:
            visited[node] = count
            count += 1
            
            for e in graph[node]:
                queue.append([e,count])
                
    
    
def solution(n, edge):
    
    graph = dict()
    graph = [set([]) for _ in range(n+1)]
    visited = [-1] * (n+1)

    
    for a, b in edge:
        graph[a].add(b)
        graph[b].add(a)
        
    dfs_sequence = bfs(graph, 1, visited)
    
    maximum = max(visited)
    
    answer = 0
    for i in visited:
        if i == maximum:
            answer += 1
            
    return answer