# 2292 벌집
# 벌집이 형성되는 규칙에 따라 벌집의 위치를 구하는 문제


count = 0
room_count = 1

n = int(input())

if n == 1:
    print(room_count)
else:
    room_count += 1
    for i in range(2, n):
        count += 1
        if count == (room_count - 1) * 6:
            count = 0
            room_count += 1
            
    print(room_count)