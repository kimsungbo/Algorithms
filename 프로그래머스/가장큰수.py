def solution(numbers):
    
    # 모든 원소가 0일경우 -> 0
    if 0 in set(numbers) and len(set(numbers)) == 1:
        return "0"
    
    
    number_list = []
    
    for num in numbers:
        temp_num = str(num)

        
        while True:
            temp_num += temp_num
            if len(temp_num) > 4:
                number_list.append([int(temp_num[0:4]), num])
                break
                
    number_list = sorted(number_list, key = lambda x: (x[0], x[-1]), reverse=True)

    ans = ''
    
    for rep, num in number_list:
        ans += ''.join(str(num))
    
    return ans