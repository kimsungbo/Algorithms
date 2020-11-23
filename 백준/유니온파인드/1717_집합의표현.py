# 1717 집합의 표현
# 유니온 파인드(disjoint set)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parents = [i for i in range(n+1)]

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
        
for i in range(m):
    x, a, b = map(int, input().split())
    
    if x == 0:
        Union(a, b)
    elif x == 1:
        a_parents = Find(a)
        b_parents = Find(b)
        if a_parents == b_parents:
            print("YES")
        else:
            print("NO")