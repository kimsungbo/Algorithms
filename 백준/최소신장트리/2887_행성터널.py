# 2887 행성 터널
# 고려할 간선의 개수를 줄임으로써 푸는 문제

import sys

input = sys.stdin.readline

N = int(input())

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
        
coords = []
for i in range(1, N+1):
    a, b, c= map(int, input().split())
    coords.append([a, b, c, i])

edges = []
for j in range(3):
    coords.sort(key=lambda x:x[j])#각 좌표별로 정렬
    
    before_location=coords[0][3]
    for i in range(1,N):#각 좌표별로 간선추가
        cur_location=coords[i][3]
        edges.append([abs(coords[i][j]-coords[i-1][j]),before_location,cur_location])
        before_location=cur_location

    
edges.sort(key = lambda x:x[0])


MST = []
parents = [i for i in range(N+1)]

count = 0
for edge in edges:
    w, u, v = edge

    if Find(u) != Find(v):
        Union(u, v)
        MST.append(edge)
        count += 1
        
    if count == N-1:
        break

print(sum([w for w, u, v in MST]))