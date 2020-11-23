def solution(land):
    score = [[0 for i in range(4)] for i in range(len(land))]
    
    score[0] = land[0]
    
    
    for k in range(1, len(land)):
        for i in range(len(score[1])):
            temp = [land[k][i] + score[k-1][j] for j in range(4) if j != i]
            score[k][i] = max(temp)
        
    
    return max(score[len(land) - 1])