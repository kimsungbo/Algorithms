# 1774 우주신과의 교감
# 이미 사용된 간선이 있을 때 최소 비용으로 나머지를 완성하는 문제

import math
from collections import deque
import sys

input = sys.stdin.readline

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

N, M = map(int, input().split())

coords = []
for i in range(1,N+1):
    x, y = map(int, input().split())
    
    coords.append([x, y, i])
    
connected = []
for _ in range(M):
    connected.append(list(map(int, input().split())))
    
edges = []
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        x1, y1 = coords[i][0], coords[i][1]
        x2, y2 = coords[j][0], coords[j][1]
        
        dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        edges.append([dist, coords[i][2], coords[j][2]])
        
edges.sort(key = lambda x:x[0])


MST = []
parents = [i for i in range(N+1)]

for edge in connected:
    u, v = edge
    
    if Find(u) != Find(v):
        Union(u, v)
        
for edge in edges:
    w, u, v = edge

    if Find(u) != Find(v):
        Union(u, v)
        MST.append(edge)

print('%0.2f' % sum([w for w, u, v in MST]))