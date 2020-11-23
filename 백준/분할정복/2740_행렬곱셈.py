# 2740 행렬 곱셈

n, m = map(int, input().split())

matrixA = []
for _ in range(n):
    matrixA.append(list(map(int, input().split())))
    
m, k = map(int, input().split())
matrixB = []

for _ in range(m):
    matrixB.append(list(map(int, input().split())))
    
ans = 0

for N in range(n):
    for K in range(k):
        for M in range(m):
            ans += matrixA[N][M] * matrixB[M][K]
        print(ans, end = ' ')
        ans = 0
    print()