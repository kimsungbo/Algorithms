from collections import deque

def solution(people, limit):
    people = sorted(people, reverse = True)
    people = deque(people)
    
    answer = 0
    
    print(people)
    
    while len(people) >= 2:
        if people[0] + people[-1] <= limit:
            answer += 1
            people.popleft()
            people.pop()
            
        else:
            answer += 1
            people.popleft()
        
        if len(people) == 1:
            answer += 1
    
    
    return answer