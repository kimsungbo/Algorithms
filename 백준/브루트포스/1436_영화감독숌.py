# 1436 영화감독 숌
# N번째 종말의 수가 나올때까지 차례대로 시도하는 문제

n = int(input())

default = 666
count = 0

while True:
    if("666" in str(default)):
        count+=1
    if(count == n):
        print(default)
        break
    default+=1