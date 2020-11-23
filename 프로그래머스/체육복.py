def solution(n, lost, reserve):
    
    for i in range(1, n+1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
        
    
    for student in reserve:
        if student - 1 in lost:
            lost.remove(student-1)
        elif student + 1 in lost:
            lost.remove(student+1)
    
    return n - len(lost)