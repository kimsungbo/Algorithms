# 2231 분해합
# 모든 경우를 시도하여 N의 생성자를 구하는 문제

n = int(input())

ans = 0
for i in range(1, n):
    if(i + sum(int(x) for x in str(i)) == n):
        ans = i
        break
        
print(ans)