# 11866 요세푸스 문제 0
# 큐를 이용해 제거 과정을 구현하는 문제

from collections import deque

n, m = map(int, input().split())

queue = deque()
remove_list = []

for i in range(1, n+1):
    queue.append(i)

while queue:
    queue.rotate(-(m-1))
    remove_list.append(queue.popleft())
    
print('<', end = "")
for i in range(len(remove_list)):
    if i != len(remove_list) - 1:
        print(remove_list[i], ', ', sep="",  end = "")
    else:
        print(remove_list[i] , end="")
print('>')