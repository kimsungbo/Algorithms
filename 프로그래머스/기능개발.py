def solution(progresses, speeds):
    
    time = []
    
    for i in range(len(progresses)):
        if (100-progresses[i]) % speeds[i] == 0:
            time.append((100-progresses[i]) // speeds[i])
        else:
            time.append((100-progresses[i]) // speeds[i] + 1)

    print(time)
    start = 0
    answer = []
    
    for i in range(len(time)):
        if time[start] < time[i]:
            answer.append(i - start)
            start = i
            
            
    answer.append(len(time)-start)
    return answer