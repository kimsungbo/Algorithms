def Find(x):
    global parents
    if x == parents[x]:
        return x
    else:
        y = Find(parents[x])
        parents[x] = y
        return y
    
def Union(x, y):
    global parents
    x = Find(x)
    y = Find(y)
    if x != y :
        parents[y] = x

def solution(n, costs):
    graph = []
    
    for u, v, w in costs:
        graph.append([u, v, w])
        
    global parents 
    parents = [i for i in range(n+1)]
    
    graph.sort(key = lambda x:x[2])
    
    MST = []
    
    for edge in graph:
        u, v, w = edge
        
        if Find(u) != Find(v):
            Union(u, v)
            MST.append(edge)
            
    return sum([w for u, v, w in MST])