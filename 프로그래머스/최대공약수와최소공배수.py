def factors(n, m):
    factor_list = []
    for i in range (2, max(n + 1, m+1)):
        while n % i == 0 and m % i == 0:
            factor_list.append(i)
            n = n // i
            m = m // i
    return factor_list

def solution(n, m):

    answer = []

    GCD_list = factors(n, m)

    GCD = 1
    for d in GCD_list:
        GCD = GCD * d

    answer.append(GCD)

    LCM = GCD * (n // GCD) * (m // GCD)
    answer.append(LCM)
    
    return answer