# 2748 피보나치 수 2
# 동적계획법으로 피보나치 수를 계산하는 문제

def fibo(x, dictionary):
    if x in dictionary:
        return dictionary[x]
    dictionary[x] = fibo(x-1, dictionary) + fibo(x-2, dictionary)
    return dictionary[x]

memo = {0:0, 1:1}
n = int(input())

print(fibo(n, memo))

