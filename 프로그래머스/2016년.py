def solution(a, b):
    
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    
    total_days = 0
    for i in range(a -1):
        total_days += days[i]
        
    total_days += b
    
    print(total_days)
    
    answer = date[(total_days + 4) % 7]

    print(answer)
    
    return answer