# 1992 쿼드 트리
# 쿼드트리 -> 문자열

n = int(input())

matrix = []

for _ in range(n):
    temp = list(str(input()))
    matrix.append([int(i) for i in temp])
        
def quad_tree(x, y, n):
    
    color = matrix[x][y]
    flag = True
    
    for i in range(x, x+n):
        if not flag:
            break
        for j in range(y, y+n):
#             print(i, j)
            if color != matrix[i][j]:
                flag = False
                print('(', sep= "", end = "")
                quad_tree(x, y, n // 2)
                quad_tree(x, y+n // 2, n//2)
                quad_tree(x + n // 2, y, n//2)
                quad_tree(x + n // 2, y + n // 2, n // 2)
                print(')', sep = "", end = "")
                break
            
    if flag:
        if color:
            print(1, sep="", end = "")
        else:
            print(0, sep="", end="")


quad_tree(0, 0, n)