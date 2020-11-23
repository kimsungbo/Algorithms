# 10816 숫자카드2
# 이분 탐색으로 값의 개수 찾기

import sys
from collections import Counter

    
n = sys.stdin.readline()
N = sys.stdin.readline().split()
m = sys.stdin.readline()
M = sys.stdin.readline().split()

C = Counter(N)
print(' '.join(f'{C[m]}' if m in C else '0' for m in M))