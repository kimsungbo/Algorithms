def solution(x):
    string = str(x)
    
    temp = [int(string[i]) for i in range(len(string))]
    
    return x % sum(temp) == 0