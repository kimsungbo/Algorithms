def solution(n):
    x = -1
    y = 0
    
    result = [[0] * n for _ in range(n)]
    
    count = 1
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
                
            result[x][y] = count
            count += 1
                
    answer = []
    
    for row in result:
        for i in row:
            if i != 0:
                answer.append(i)
    return answer