# 2252 줄세우기
# 순서가 정해져 있는 작업을 차례로 수행해야 할때 그 순서를 결정해 주기 위해 사용하는 알고리즘
# Directed Acyclic Graph에만 적용 가능

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

inDegree = [0] * (N + 1)

def topologySort(graph, inDegree):
    queue = []
    result = []
    
    for i in range(1, len(inDegree)) :
        if inDegree[i] == 0:
            queue.append(i)
            
            
    # 정렬이 완전히 수행되려면 정확히 n개의 노드를 방문해야하는데
    for i in range(1, N + 1):
        # 그 전에 queue가 비어버리면 사이클 발생
        if not queue:
            return
        
        x = queue.pop(0)
        result.append(x)
        
        
        for j in range(len(graph[x])):
            temp_indegree = graph[x][j]
            
            # 현재노드를 없앴을때 indegree가 0이되는 node를 큐에 삽입
            inDegree[temp_indegree] -= 1
            if inDegree[temp_indegree] == 0:
                queue.append(temp_indegree)
                
    return result
        
graph = [[] for i in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    inDegree[B] += 1

    
sorted_list = topologySort(graph, inDegree)
print(*sorted_list)