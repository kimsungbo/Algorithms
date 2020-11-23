# 10830 행렬 제곱
# 분할 정복으로 행렬의 거듭제곱을 빠르게 계산하는 문제

def matrix_mul(mat1, mat2, x):
    
    result = [[0] * x for _ in range(x)]
    
    for i in range(x):
        for j in range(x):
            for k in range(x):
                result[i][j] += mat1[i][k] * mat2[k][j]

    for i in range(x):
        for j in range(x):
            result[i][j] %= 1000
    
    return result

def power(mat, n, b):
    if b == 1: 
        return mat
    elif b == 2:
        return matrix_mul(mat, mat, n)
    else:   
        temp = power(matrix, n, b // 2)
        if b % 2 == 0:
            return matrix_mul(temp, temp, n) # b가 짝수인 경우
        else:
            return matrix_mul(matrix_mul(temp, temp, n), matrix, n) # b가 홀수인 경우
        
N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

final_matrix = power(matrix, N, B)

for i in range(N):
    for j in range(N):
        final_matrix[i][j] %= 1000
            
for row in final_matrix:
    print(*row)