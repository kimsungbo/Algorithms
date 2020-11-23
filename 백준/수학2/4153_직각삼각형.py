# 4153 직각삼각형
# 피타고라스의 정리

while 1:
    num_list = list(map(int, input().split()))
    
    if 0 not in num_list:
        new_num_list = [x*x for x in num_list]
        max_index = new_num_list.index(max(new_num_list))
        sum = 0
        for i in range(0, len(new_num_list)):
            if i != max_index:
                sum += new_num_list[i]
                
        
        if(max(new_num_list) == sum):
            print('right')
        else:
            print('wrong')

    else:
        break