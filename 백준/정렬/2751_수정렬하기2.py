# 2751 수 정렬하기 2
# O(nlogn)
# ex) 병합정렬, 힙정렬

import sys

n = int(input())

num_list = []

for i in range(n):
    num_list.append(int(sys.stdin.readline()))
    
for i in sorted(num_list):
    print(str(i), end='\n')