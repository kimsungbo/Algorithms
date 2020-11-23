# 1976 여행 가자
# 유니온 파인드로 두 정점이 연결되어 있는지 확인

cities = int(input())
travel = int(input())

parents = [i for i in range(cities+1)]



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
        
for y in range(1, cities+ 1):
    maps = list(map(int, input().split()))
    
    for x in range(1, len(maps) + 1):
        if maps[x-1] == 1:
            Union(y, x)
            
tour = list(map(int, input().split()))
result = set([Find(i) for i in tour])


if len(result ) != 1:
    print("NO")
else:
    print("YES")