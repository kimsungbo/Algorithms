# 4368 별자리 만들기
# 좌표평면에서 MST를 만드는 문제

import math

n = int(input())

coords = []
for i in range(1,n+1):
    x, y = map(float, input().split())
    coords.append([x, y, i])
        
edges = []
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        x1, y1 = coords[i][0], coords[i][1]
        x2, y2 = coords[j][0], coords[j][1]
        
        dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        edges.append([dist, coords[i][2], coords[j][2]])
        
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

edges.sort(key = lambda x:x[0])

parents = [i for i in range(n+1)]

MST = []
for edge in edges:
    w, u, v = edge

    if Find(u) != Find(v):
        Union(u, v)
        MST.append(edge)

print('%0.2f' % sum([w for w, u, v in MST]))