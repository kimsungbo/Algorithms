def solution(s):
    num_list = s.split()
    num_list = [int(num_list[i]) for i in range(len(num_list))]
    
    
    return str(min(num_list)) + " " + str(max(num_list))