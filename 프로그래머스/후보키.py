from itertools import combinations

def solution(relation):
    answer = 0
    
    column = [i for i in range(len(relation[0]))]

    combi = []
    for i in range(1, len(relation[0])+ 1):
        combi.extend([set(k) for k in combinations(column, i)])

    print(combi)

    combi_set = []
    for comb in combi:
        temp_list = []
        temp = ""
        for row in relation:
            for c in comb:
                temp += row[c]
            temp_list.append(temp)
            temp = ''
        if(len(temp_list) == len(set(temp_list))):
            combi_set.append(comb)
            
    print(combi_set)
    
    del_set = []
    
    for i in range(len(combi_set)):
        for j in range(len(combi_set)):
            if i != j and combi_set[i].issubset(combi_set[j]):
                if combi_set[j] not in del_set:
                    del_set.append(combi_set[j])
                
    print(del_set)
    
    return len(combi_set) - len(del_set)