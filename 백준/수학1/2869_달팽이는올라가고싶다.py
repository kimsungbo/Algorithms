# 2869 달팽이는 올라가고 싶다
# 달팽이의 움직임을 계산하는 문제

import math

a, b, v = map(int, input().split())

remaining = v

if a > v:
    print(1)

else:
    print(math.ceil((v-a)/(a-b)) + 1)