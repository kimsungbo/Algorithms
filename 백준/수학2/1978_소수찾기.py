# 1978 소수찾기
# 주어진 값보다 작은수중 소수 찾기

n = int(input())

def is_prime(x):
    # 2이상의 숫자들로 나눠지면 소수가 아님
    if num != 1:
        for i in range(2, num):
            if(num % i == 0):
                return False
    else:
        return False
    return True

num_list = list(map(int,input().split()))

num_prime = 0;

for num in num_list:
    if is_prime(num):
        num_prime +=1

print(num_prime)