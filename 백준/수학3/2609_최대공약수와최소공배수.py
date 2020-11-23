# 2609 최대공약수와 최소공배수

x, y = map(int, input().split())

def factors(n, m):
    factor_list = []
    for i in range (2, max(n + 1, m+1)):
        while n % i == 0 and m % i == 0:
            factor_list.append(i)
            n = n // i
            m = m // i
    return factor_list
            
GCD_list = factors(x, y)

GCD = 1
for d in GCD_list:
    GCD = GCD * d

print(GCD)

LCM = GCD * (x // GCD) * (y // GCD)
print(LCM)