# 12015 가장 긴 증가하는 부분수열 2

import sys
input = sys.stdin.readline

# x = 찾으려는값
def lower_bound(arr, start, end, x):
    while start < end:
        mid = (start + end ) // 2
        
        if arr[mid] < x:
            start = mid + 1
        else:
            end = mid
            
    return end

n = int(input())
seq = list(map(int, input().split()))
answer = []

for num in seq:
    if len(answer) == 0:
        answer.append(num)
        
        
    if answer[-1] < num:
        answer.append(num)
        
    else:
        idx = lower_bound(answer, 0, len(answer) - 1, num)
        answer[idx] = num
        
print(len(answer))