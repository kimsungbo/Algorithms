from collections import deque

def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))
    return visited


def solution(n, computers):
    graph = [set([]) for _ in range(n+1)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i+1].add(j+1)
                
    print(graph)
    
    temp_list = [i for i in range(1, n+1)]
    print('temp_list', temp_list)
    
    count = 0
    start = -1
    while temp_list:
        start = temp_list[0]
        bfs_sequence = bfs(graph, start)
        temp_list = [x for x in temp_list if x not in bfs_sequence]
        print(temp_list)
        count += 1
        
    return count