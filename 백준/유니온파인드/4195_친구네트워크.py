# 4195 친구 네트워크
# 유니온 파인드에 집합의 크기를 구하는 기능을 넣는 문제

import sys
input = sys.stdin.readline

t = int(input())


def Find(parents, x):
    if x == parents[x]:
        return x
    p = Find(parents, parents[x])
    parents[x] = p
    return parents[x]

def Union(parents, a, b, cnt):
    x = Find(parents, a)
    y = Find(parents, b)
    if x != y :
        parents[y] = x
        cnt[x] += cnt[y]

    
for i in range(t):
    f = int(input())
    parents = {}
    cnt = {}
    for j in range(f):
        a, b = map(str, input().split())

        if a not in parents:
            parents.setdefault(a, a)
            cnt[a] = 1
        if b not in parents:
            parents.setdefault(b, b)
            cnt[b] = 1
                
        
        Union(parents, a, b, cnt)
        
        print(cnt[Find(parents, a)])