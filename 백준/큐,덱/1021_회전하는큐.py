# 1021 회전하는 큐
# 덱을 활용하여 큐를 회전시키는 문제


from collections import deque

n, m = map(int, input().split())

def to_left(num_list, num):
    temp = num_list.copy()
    count = 0
    while True:
        if temp[0] == num:
            break
        else: 
            temp.rotate(-1)
            count+=1
    return count

def to_right(num_list, num):
    temp = num_list.copy()
    count = 0
    while True:
        if temp[0] == num:
            break
        else: 
            temp.rotate(+1)
            count+=1
    return count

queue = deque()

for i in range(1, n+1):
    queue.append(i)

element_coord = list(map(int, input().split()))

sum = 0
for element in element_coord:
    left = to_left(queue, element)
    right = to_right(queue, element)
    sum = sum + min(left, right)
    if left > right:
        queue.rotate(-left)
        queue.popleft()
    else:
        queue.rotate(+right)
        queue.popleft()
    
print(sum)