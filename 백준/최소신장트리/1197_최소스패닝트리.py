# 1197 최소 스패닝 트리
# MST(가중치 합이 최소인 최소 신장 트리)

def Find(x):
    if x == parents[x]:
        return x
    else:
        y = Find(parents[x])
        parents[x] = y
        return y
    
def Union(x, y):
    x = Find(x)
    y = Find(y)
    if x != y :
        parents[y] = x
        
graph = []

V, E = map(int, input().split())

for _ in range(E):
    A, B, C = map(int, input().split())
    graph.append([A, B, C])
    
parents = [i for i in range(V+1)]
    
# 가중치 오름차순으로 간선을 정렬
graph.sort(key = lambda x: x[2])

MST = []

for edge in graph:
    u, v, w = edge

    if Find(u) != Find(v):
        Union(u, v)
        MST.append(edge)
        
print(sum([w for u, v, w in MST]))