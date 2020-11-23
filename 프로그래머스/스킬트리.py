def solution(skill, skill_trees):
    answer = 0
    for node in skill_trees:
        temp = []
        for i in range(len(node)):
            if node[i] in skill:
                temp.append(node[i])
        
        temp = [skill.index(temp[i]) for i in range(len(temp))]
        
        sorted_temp = sorted(temp)
        
        if temp == sorted_temp:
            print(all(i in node for i in skill[:len(temp)]))
            if all(i in node for i in skill[:len(temp)]):
                answer += 1
    
    return answer