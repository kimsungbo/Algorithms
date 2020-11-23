def solution(record):
    dictionary = dict()
    answer = []
    
    for r in record:
        r = r.split()
        
        if r[0] == 'Enter':
            dictionary[r[1]] = r[2]
        elif r[0] == "Change":
            dictionary[r[1]] = r[2]
            
    
    for r in record:
        r = r.split()
        temp = ""
        if r[0] == 'Enter':
            answer.append(dictionary[r[1]] + "님이 들어왔습니다.")
        elif r[0] == 'Leave':
            answer.append(dictionary[r[1]] + "님이 나갔습니다.")
            
    return answer