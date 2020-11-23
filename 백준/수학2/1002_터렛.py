# 1002 터렛
# 두 원의 교점의 개수를 구하는 문제

import math

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    
    distance = math.sqrt(((x1 - x2) ** 2 )+ ((y1 - y2) ** 2))
    r_sum = r1+ r2
    
    # a, b의 좌표가 같은경우
    if x1 == x2 and y1 == y2:
        
        # 반지름이 같으면 무수히 많은 곳에서 겹칠 수 있음
        if r1 == r2:
            print(-1)
        
        # 반지름이 다르면 겹칠수 없음
        else:
            print(0)
            
    # a,b 의 좌표가 다른 경우        
    else:
        
        # a,b의 거리가 두 반지름의 합보다 크면 겹치는 지점 없음
        if distance > r_sum:
            print(0)
            
        # a, b의 거리가 두반지름의 합이랑 같다면 한곳에서 겹침
        elif distance == r_sum:
            print(1)
            
        
        # a, b의 거리가 두 반지름의 합보다 작다면
        elif distance < r_sum:
            
            if (distance + min(r1, r2)) == max(r1, r2):
                print(1)
                
            elif(distance + min(r1, r2)) < max(r1, r2):
                print(0)
                
            else:
                print(2)