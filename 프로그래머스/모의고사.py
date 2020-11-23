def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4 ,5,  5]
    
    right = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == person1[i % 5]:
            right[0] += 1
        if answers[i] == person2[i % 8]:
            right[1] += 1
        if answers[i] == person3[i % 10]:
            right[2] += 1
            
    print(right)
    
    maximum_score = max(right)
    
    ans = []
    for i in range(len(right)):
        if right[i] == maximum_score:
            ans.append(i+1)

    ans = sorted(ans)
    print(ans)
    return ans