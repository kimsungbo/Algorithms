# 11651 좌표 정렬하기 2

n = int(input())

coord_list = []
for i in range(n):
    x, y = map(int, input().split())
    coord_list.append([x, y])

for item in sorted(coord_list, key = lambda x : (x[1], x[0])):
    print(item[0], item[1])