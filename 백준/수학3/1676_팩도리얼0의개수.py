# 1676 팩도리얼 0의 개수
# 소인수분해의 성질을 활용하여 N!의 끝에 0이 얼마나 많이 나오는지 구하는 문제

from math import factorial

fac = factorial(int(input()))

lst = list(map(int, str(fac)))

num_zero = 0
for i in range(len(lst) - 1, 0, -1):
    if lst[i] == 0:
        num_zero += 1
    
    if lst[i-1] != 0:
        break

print(num_zero)