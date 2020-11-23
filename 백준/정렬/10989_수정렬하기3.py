# 10989 수 정렬하기 3
# 카운팅정렬

import sys

n = int(input())

num_list = [0] * 10001

for i in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(len(num_list)):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)