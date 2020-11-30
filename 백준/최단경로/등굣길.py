def solution(m, n, puddles):
    map = [[0 for i in range(m)] for j in range(n)]
    
    map[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if [j+1, i+1] in puddles:
                map[i][j] = 0
            else:
                map[i][j] = map[i-1][j] + map[i][j-1]
                
    print(map)
    return map[n-1][m-1] % 1000000007
    
    