def solution(d, budget):
    d = sorted(d)
    
    if sum(d) <= budget:
        return len(d)
    elif d[0] > budget:
        return 0
    
    for i in range(len(d)):
        budget -= d[i]
        
        if budget == 0:
            return i + 1
        elif budget < 0:
            return i