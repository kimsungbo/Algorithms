# 2750 수 정렬하기
# O(n^2)
# ex) 삽입정렬, 거품정렬

n = int(input())

num_list = []
for i in range(n):
    num_list.append(int(input()))
    
num_list = sorted(num_list)

for num in num_list:
    print(num)