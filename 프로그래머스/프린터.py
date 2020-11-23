def solution(priorities, location):    
    
    idx = list(range(len(priorities)))
    idx[location] = 'target'
    
    order = 0
    
    while True:
        if priorities[0] == max(priorities):
            order += 1
            
            if (idx[0] == 'target'):
                return order
            
            else:
                x = priorities.pop(0)
                idx.pop(0)
        else:
            priorities.append(priorities.pop(0))
            idx.append(idx.pop(0))