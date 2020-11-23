def solution(N, stages):
    answer = []
    
    unsolved = [0] * (N+1)
    reached = [0] * (N+1)
        
    
    for stage in stages:
        
        if stage > N:
            reached = [reached[i]+1 for i in range(len(reached))]
        else:
            unsolved[stage] += 1
            for i in range(1, stage + 1):
                reached[i] += 1
            
    
    
    for i in range(1, N+1):
        if unsolved[i] == 0 or reached[i] == 0:
            answer.append([i, 0])
        else:
            answer.append( [i, unsolved[i] / reached[i]])
            
    answer = sorted(answer, key = lambda x: x[1], reverse=True)
    
    final_answer = []
    for an in answer:
        final_answer.append(an[0])
    
    return final_answer