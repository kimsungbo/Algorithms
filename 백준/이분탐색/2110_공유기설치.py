# 2110 공유기 설치

import sys
input = sys.stdin.readline

n, c = map(int, input().split())

house_list = [int(sys.stdin.readline()) for _ in range(n)]

    
house_list = sorted(house_list)

start = 1
end = house_list[-1] - house_list[0]

def router_counter(distance):
    count = 1
    current_house = house_list[0] #시작 집
    
    for i in range(1, n): # 모든집 탐방시작
        # 이전집에서 해당 집까지 거리가 distance보다 멀다면 설치 가능
        if current_house + distance <= house_list[i]:
            count += 1
            current_house = house_list[i]
    return count

while start <= end:
    mid = (start + end ) // 2
#     print(start, end, mid)
#     print('num_router', router_counter(mid))
    
    if router_counter(mid) >= c:
        answer = mid
        start = mid + 1
        
    else:
        end = mid - 1
        
print( answer)

