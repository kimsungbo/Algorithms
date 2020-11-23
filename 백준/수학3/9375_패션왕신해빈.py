# 9375 패션왕 신해빈
# 경우의 수 연습 문제

t = int(input())

for _ in range(t):
    n = int(input())
    
    dictionary = dict()
    for _ in range(n):
        name, clothType = map(str, input().split())
        if clothType in dictionary:
            dictionary[clothType] +=1 
            
        else:
            dictionary[clothType] = 1
            

    ans = 1
    for item in dictionary:
        ans *= (dictionary[item] + 1)
        
    print(ans-1)