# 10870 피보나치수

n = int(input())

def fibo(n):
    if n == 0:
        return 0
    if n < 3:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
        
print(fibo(n))