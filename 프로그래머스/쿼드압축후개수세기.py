def quad_tree(arr, x, y, n):
    
    answer = ""
    
    color = arr[x][y]
    flag = True
    
    for i in range(x, x+n):
        if not flag:
            break
        for j in range(y, y+n):
#             print(i, j)
            if color != arr[i][j]:
                flag = False
                answer += "("
                answer += quad_tree(arr, x, y, n // 2)
                answer += quad_tree(arr, x, y+n // 2, n//2)
                answer += quad_tree(arr, x + n // 2, y, n//2)
                answer += quad_tree(arr, x + n // 2, y + n // 2, n // 2)
                answer += ")"
                break
            
    if flag:
        if color:
            answer += "1"
        else:
            answer += "0"
            
    return answer


            
def solution(arr):
    n = len(arr)
    answer = quad_tree(arr, 0, 0, n)
    
    return [answer.count("0"), answer.count("1")]