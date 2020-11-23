def solution(brown, yellow):
    
    total = brown + yellow
    factor_list = []
    
    for i in range(1, total + 1):
        if total % i == 0 :
            factor_list.append(i)
            
    print(factor_list)
    
    if len(factor_list) % 2 != 0:
        mid = len(factor_list) // 2
        for i in range(len(factor_list) // 2):
            if  i == 0:
                if (factor_list[mid] - 2 ) ** 2 == yellow:
                    return [factor_list[mid], factor_list[mid]]
            else:
                if( factor_list[mid - i] - 2) * ( factor_list[mid + i] - 2) == yellow:
                    return [( factor_list[mid + i]), ( factor_list[mid - i])]
                
    else:
        mid = len(factor_list) // 2
        left = list(reversed(factor_list[:mid]))
        right = factor_list[mid:]
        print(left, right)
        
        for i in range(mid):
            if (left[i] - 2) * (right[i] - 2) == yellow:
                return [right[i], left[i]]
        
    
            
    
    return 0