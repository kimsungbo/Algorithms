# 10814 나이순 정렬
# 값이 같은 원소의 전후관계가 바뀌지 않는 정렬 = stable sort

from operator import itemgetter

n = int(input())

member_list = []
for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    member_list.append([age, name])
    
for item in sorted(member_list, key=itemgetter(0)):
    print(item[0], item[1])