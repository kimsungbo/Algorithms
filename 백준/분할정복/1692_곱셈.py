# 1692 곱셈
# 분할정복으로 거듭제곱을 빠르게 계산하는 문제

def power(a, b):
    if b == 1: # b의 값이 1이면 a % C를 return한다.
        return a % C
    else:
        temp = power(a, b // 2) # a^(b // 2)를 미리 구한다.
        if b % 2 == 0:
            return temp * temp % C # b가 짝수인 경우
        else:
            return temp * temp * a % C # b가 홀수인 경우

A, B, C = map(int, input().split())

result = power(A, B)
print(result)