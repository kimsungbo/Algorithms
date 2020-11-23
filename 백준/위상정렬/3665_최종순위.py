# 3665 최종 순위
# 간선을 직접 정의한 다음 위상정렬을 하는 문제

T = int(input())

def topologySort(graph, inDegree, N):
    queue = []
    result = []
    
    for i in range(1, len(inDegree)) :
        if inDegree[i] == 0:
            queue.append(i)
            
#     print('queue', queue)
            
            
    # 정렬이 완전히 수행되려면 정확히 n개의 노드를 방문해야하는데
    for i in range(1, N + 1):
        # 그 전에 queue가 비어버리면 사이클 발생
        if not queue:
            return -1
        
        x = queue.pop(0)
        result.append(x)
        
        
        for j in range(len(graph[x])):
            temp_indegree = graph[x][j]
            
            # 현재노드를 없앴을때 indegree가 0이되는 node를 큐에 삽입
            inDegree[temp_indegree] -= 1
            if inDegree[temp_indegree] == 0:
                queue.append(temp_indegree)
                
    return result

for _ in range(T):
        
    n = int(input())
    ti = list(map(int, input().split()))
    m = int(input())
    
    graph = [[] for i in range(len(ti) + 1)]
    inDegree = [0 for i in range(len(ti) + 1)]
    
    for i in range(len(ti) + 1):
        for j in range(i+1, len(ti)):
            graph[ti[i]].append(ti[j])
            inDegree[ti[j]] += 1          
            
#     print('graph', graph)
#     print('indegree', inDegree)

    for _ in range(m):
        a, b = map(int, input().split())
        
        if b in graph[a]:
            graph[a].remove(b)
            graph[b].append(a)
            inDegree[b] -= 1
            inDegree[a] += 1
        elif a in graph[b]:
            graph[b].remove(a)
            graph[a].append(b)
            inDegree[a] -= 1
            inDegree[b] += 1
            
#         print(graph)
#         print(inDegree)
        
    sorted_list = topologySort(graph, inDegree, n)
    if sorted_list == -1:
        print('IMPOSSIBLE')
    else:
        print(*sorted_list)