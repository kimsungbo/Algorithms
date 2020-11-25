def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):
    
    converted = ''
    
    num = 0
    while num <= t * m:
        converted += convert(num, n)
        num += 1
        
    converted = [converted[i * m:(i + 1) * m] for i in range((len(converted) + m - 1) // m )]
                 
                 
    answer = ''
    
    for i in range(len(converted) - 1):
        answer += converted[i][p-1]
    
    return answer[:t]