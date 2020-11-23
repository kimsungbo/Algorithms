def conv(number,base):
    T="0123456789ABCDEF"
    i,j=divmod(number,base)
    
    if i==0:
        return T[j]
    else:
        return conv(i,base)+T[j]

def solution(n):
    base3 = conv(n, 3)
    
    answer = 0
    
    for i in range(0, len(base3)):
        print(base3[i])
        answer += int(base3[i]) * (3 ** i)
    
    return answer