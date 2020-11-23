# 2630 색종이 만들기
# 쿼드 트리

n = int(input())

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

def quad_tree(x, y, n):
    global count_one, count_zero
    
    color = matrix[x][y]
    flag = True
    
    for i in range(x, x+n):
        if not flag:
            break
        for j in range(y, y+n):
            if color != matrix[i][j]:
                flag = False
                quad_tree(x, y, n // 2)
                quad_tree(x, y+n // 2, n//2)
                quad_tree(x + n // 2, y, n//2)
                quad_tree(x + n // 2, y + n // 2, n // 2)
                break
            
    if flag:
        if color:
            count_one += 1
        else:
            count_zero += 1

count_one = 0
count_zero = 0

quad_tree(0, 0, n)


print(count_zero)
print(count_one)