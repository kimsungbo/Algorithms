# 1003 피보나치 함수


zeros = [1, 0, 1]
ones = [0, 1, 1]

def fibonacci(n):
    if len(zeros) <= n:
        for i in range(len(zeros), n+1):
            zeros.append(zeros[i-1] + zeros[i-2])
            ones.append(ones[i-1] + ones[i-2])
            
    print(zeros[n], ones[n])
    
t = int(input())

for i in range(t):
    n = int(input())
    fibonacci(n)