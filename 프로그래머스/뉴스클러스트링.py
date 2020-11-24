import re
import math

def solution(str1, str2):
    str1 = [str1.lower()[i:i+2] for i in range(0, len(str1) - 1)]
    str2 = [str2.lower()[i:i+2] for i in range(0, len(str2) - 1)]
    
    regex = re.compile('[^a-zA-Z]')
    set1 = []
    set2 = []
    
    for i in range(len(str1)):
        temp = regex.sub('', str1[i])
        if temp != '' and len(temp) > 1:
            set1.append(temp)
        

    for i in range(len(str2)):
        temp = regex.sub('', str2[i])
        if temp != '' and len(temp) > 1:
            set2.append(temp)
        
    
    
    set3 = []
    set3.extend(set1)
    set3.extend(set2)
    set3 = list(set(set3))

    if len(set1) == 0 and len(set2) == 0:
        return 65536
    elif len(set1) == len(set(set1)) and len(set2) == len(set(set2)):
        inter = [val for val in set1 if val in set2]
        return math.floor(len(inter) / len(set3) * 65536)
    else:
        
        dict1 = dict()
        dict2 = dict()
        
        for i in set1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
                
        for i in set2:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1
        
        intersection_list = []
        union_dict = dict1
        
        for i in dict1:
            if i in dict2:
                for j in range(min(dict1[i], dict2[i])):
                    intersection_list.append(i)

        for i in dict2:
            if i in union_dict:
                if dict2[i] > union_dict[i]:
                    union_dict[i] = dict2[i]
            else:
                union_dict[i] = dict2[i]
                    
        union_list = []
        
        for i in union_dict:
            for j in range(union_dict[i]):
                union_list.append(i)
                
        
        return math.floor(len(intersection_list) / len(union_list) * 65536)