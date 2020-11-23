# 1780 종이의 개수
# 쿼드트리와 비슷하지만 4개 대신 9개로 나누는 문제

n = int(input())

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

def quad_tree(x, y, n):
    global count_one, count_zero, count_minus
    
    color = matrix[x][y]
    flag = True
    
    for i in range(x, x+n):
        if not flag:
            break
        for j in range(y, y+n):
            if color != matrix[i][j]:
                flag = False
                quad_tree(x, y, n // 3)
                quad_tree(x, y + n // 3, n // 3)
                quad_tree(x, y + n - n // 3, n//3)
                
                quad_tree(x + n // 3, y, n//3)
                quad_tree(x + n // 3, y + n // 3, n // 3)
                quad_tree(x + n // 3, y + n - n // 3, n // 3)
                
                quad_tree(x + n - n // 3, y, n // 3)
                quad_tree(x + n - n // 3, y + n // 3, n // 3)
                quad_tree(x + n - n // 3, y + n - n // 3, n // 3)
                break
            
    if flag:
        if color == 1:
            count_one += 1
        elif color == 0:
            count_zero += 1
        elif color == -1:
            count_minus += 1
            
count_one = 0
count_zero = 0
count_minus = 0

quad_tree(0, 0, n)

print(count_minus)
print(count_zero)
print(count_one)