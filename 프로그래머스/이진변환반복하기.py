def solution(s):
    
    count = 0
    num_zero = 0
    
    while True:
        if s == "1":
            break
        else:
            num_zero += s.count("0")
            s = str(bin(s.count("1")))[2:]
            count += 1 
            
    return [count, num_zero]