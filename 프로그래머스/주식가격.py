def solution(prices):
    
    answer = []
    
    for i in range(len(prices)):
        flag = False
        for j in range(i+1, len(prices)):
            if prices[j] < prices[i]:
                answer.append(j-i)
                flag = True
                break
        if flag == False:
            answer.append(len(prices) - i - 1)
        
    return answer