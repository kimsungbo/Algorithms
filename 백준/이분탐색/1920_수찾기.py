# 1920 수 찾기
# 배열을 정렬한후 이분탐색으로 값 찾기

def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)
    
n = int(input())
N = sorted(list(map(int, input().split())))
m = int(input())
M = list(map(int, input().split()))

for l in M:
    start = 0
    end = len(N)-1
    print(binary(l,N,start,end))