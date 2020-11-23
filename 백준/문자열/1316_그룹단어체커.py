# 1316 그룹 단어 체커
# 조건에 맞는 문자열을 찾는 문제

# 문자열을 입력받아 연속되는 알파벳이 있을경우 한개만 남긴채 반환
# ex) happy -> hapy
def remove_continuing(x: str)-> list:
    string = list(x)

    dup_list = []
    for i in range(0, len(string)-1):
        if string[i] == string[i+1]:
            dup_list.append(i+1)

    print(dup_list)
    new_string = []
    for i in range(0, len(string)):
        if i not in dup_list:
            new_string.append( string[i])

    print(new_string)
    return new_string



x = int(input())

count = 0
for i in range(x):
    input_string = map(str, input())
    new_list = remove_continuing(input_string)
    
    # 연속된 알파벳 제거후 그 알파벳이 문자열 다른곳에 사용되었을 경우 = 그룹단어 X
    dictionary = {}
        
    for k in range(0, len(new_list)):
        if new_list[k] not in dictionary.keys():
            dictionary[new_list[k]] = 1
        else:
            dictionary[new_list[k]] += 1
        
    is_group_word = 1
        
        
    for k in dictionary:
        if dictionary[k] > 1:
            is_group_word = 0
                
    if is_group_word == 1:
        count+=1
    
print(count)
        