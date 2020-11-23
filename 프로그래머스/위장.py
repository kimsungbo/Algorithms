def solution(clothes):
    
    cloth_dict = dict()
    for cloth, type in clothes:
        if type in cloth_dict:
            cloth_dict[type] += 1
        else:
            cloth_dict[type] = 1
        
    print(cloth_dict)
    
    ans = 1
    for item in cloth_dict:
        ans *= (cloth_dict[item] + 1)
        
    return ans-1