from collections import deque
def solution(dartResult):
    dartResult = deque(dartResult)
    answer = [0, 0, 0]
    options = ['', '', '']
    for i in range(3):
        score = int(dartResult.popleft())
        area = ''
        if dartResult[0] not in ['S', 'D', 'T']:
            score = 10
            dartResult.popleft()
            area = dartResult.popleft()
        else:
            area = dartResult.popleft()
            

            
        print(score, area)
        
        if area == 'S':
            answer[i] = score ** 1
        elif area == 'D':
            answer[i] = score ** 2
        elif area == 'T':
            answer[i] = score ** 3
        
        print(answer)

        option = ''
        if dartResult:
            if dartResult[0] == '#' or dartResult[0] == '*':
                option = dartResult.popleft()
        
        if option == '*':
            if i == 0:
                answer[0] *= 2
            else:
                answer[i-1] *= 2
                answer[i] *= 2
        
        elif option == '#':
            answer[i] *= -1
        print(answer)
        
    print(sum(answer))
        
    return sum(answer)