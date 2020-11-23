# 3036 링
# 첫번째 링을 한바퀴 돌렸을때, 나머지 링이 몇바퀴 도는지 구하는 문제

from fractions import Fraction

n = int(input())
ring_list = list(map(int, input().split()))

for i in range(1, n):
    answer = Fraction(ring_list[0], 1) / Fraction(ring_list[i], 1)
    print(answer.numerator, '/', answer.denominator, sep='')