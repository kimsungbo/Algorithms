# 10250 ACM 호텔
# 호텔 방 번호의 규칙을 찾아 출력하는 문제

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    floor = n % h
    if floor == 0:
        floor = h
    
    room_num = ((n - 1) // h) + 1
    
    room_string = ''
    if room_num < 10:
        room_string = room_string + '0' + str(room_num)
    else:
        room_string = room_string + str(room_num)
    print(str(floor) + room_string)
    