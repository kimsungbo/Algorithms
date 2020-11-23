# 11401 이항계수3
# 분할정복을 사용한 거듭제곱과 페르마의 소정리를 이용해 곱셈의 역원을 구하는 문제

# 이항계수 3

def power(a, b, p):
    if b == 1: # b의 값이 1이면 a % C를 return한다.
        return a % p
    else:
        temp = power(a, b // 2, p) # a^(b // 2)를 미리 구한다.
        if b % 2 == 0:
            return temp * temp % p # b가 짝수인 경우
        else:
            return temp * temp * a % p # b가 홀수인 경우
    
    
n, k = map(int, input().split())
p = 1000000007

# (n k) = n! / (n-k)!k!

# n!
numerator = 1
for num in range(1, n+1):
    numerator *= num
    numerator %= p
    

denominator = 1
# (n-k)!
for num in range(1, n-k+1):
    denominator *= num
    denominator %= p    

# k!
for num in range(1, k+1):
    denominator *= num
    denominator %= p
    
denominator = power(denominator, p-2, p) %p
result = (numerator * denominator) % p
print(result)
